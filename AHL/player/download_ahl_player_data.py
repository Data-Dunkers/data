import os
import unicodedata
from pathlib import Path

import pandas as pd

SEASON_LABEL = os.getenv("AHL_SEASON_LABEL", "2025-2026")
START_YEAR = int(os.getenv("AHL_START_YEAR", "2000"))
END_YEAR = int(os.getenv("AHL_END_YEAR", "2026"))
OUTPUT_DIR = Path(__file__).resolve().parent
TEAM_PLAYERS_DIR = OUTPUT_DIR.parent / "team_players"
MOOSE_CODES = {"MTB", "MB", "MOO", "MAN", "MBM"}
MIN_EXPECTED_ROWS = int(os.getenv("AHL_MIN_EXPECTED_ROWS", "400"))
CSV_ENCODING = "utf-8-sig"
REPLACEMENT_CHAR = "\uFFFD"
MOJIBAKE_TOKENS = ("Ã", "Â", "â€™", "â€“", "â€œ", "â€")


def season_label(start_year: int) -> str:
    return f"{start_year}-{start_year + 1}"


def season_from_label(label: str) -> int:
    return int(label.split("-", maxsplit=1)[0])


def load_season_players(label: str) -> pd.DataFrame:
    season_dir = TEAM_PLAYERS_DIR / label
    files = sorted(season_dir.glob("*_players.csv"))
    if not files:
        return pd.DataFrame()
    frames = [pd.read_csv(path) for path in files]
    return pd.concat(frames, ignore_index=True)


def normalize_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    text_cols = df.select_dtypes(include=["object", "string"]).columns

    def clean_text(value: object) -> object:
        if not isinstance(value, str):
            return value
        cleaned = unicodedata.normalize("NFC", value)
        if REPLACEMENT_CHAR in cleaned:
            cleaned = cleaned.replace(REPLACEMENT_CHAR, "")
        if any(token in cleaned for token in MOJIBAKE_TOKENS):
            try:
                repaired = cleaned.encode("latin1").decode("utf-8")
                cleaned = unicodedata.normalize("NFC", repaired)
            except UnicodeError:
                pass
        return cleaned

    for col in text_cols:
        df[col] = df[col].map(clean_text)
    return df


def validate_frame(df: pd.DataFrame, label: str) -> None:
    if len(df) < MIN_EXPECTED_ROWS:
        raise ValueError(
            f"{label}: only {len(df)} rows (expected at least {MIN_EXPECTED_ROWS})."
        )
    text_cols = df.select_dtypes(include=["object", "string"]).columns
    if not len(text_cols):
        return
    has_replacement = (
        df[text_cols]
        .astype(str)
        .apply(lambda c: c.str.contains(REPLACEMENT_CHAR, regex=False))
        .any()
        .any()
    )
    if has_replacement:
        raise ValueError(
            f"{label}: found replacement characters (U+FFFD) in text fields."
        )


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    all_frames = []
    moose_frames = []
    for year in range(START_YEAR, END_YEAR + 1):
        label = season_label(year)
        season_df = load_season_players(label)
        if season_df.empty:
            continue
        season_df = normalize_text_columns(season_df)
        validate_frame(season_df, label)

        season_path = OUTPUT_DIR / f"ahl_player_stats_{label}.csv"
        season_df.to_csv(season_path, index=False, encoding=CSV_ENCODING)
        print(f"Saved {len(season_df)} rows to {season_path.name}")

        season_with_year = season_df.copy()
        season_with_year.insert(1, "Year", year)
        if "Name" in season_with_year.columns:
            ordered_cols = ["Name", "Year"] + [
                col for col in season_with_year.columns if col not in {"Name", "Year"}
            ]
            season_with_year = season_with_year[ordered_cols]
        all_frames.append(season_with_year)

        if "Team" in season_df.columns:
            moose_df = season_df[season_df["Team"].isin(MOOSE_CODES)].copy()
            if not moose_df.empty:
                moose_df.insert(0, "Season", label)
                moose_frames.append(moose_df)
                if label == SEASON_LABEL:
                    moose_path = OUTPUT_DIR / f"MB_Moose_player_stats_{label}.csv"
                    moose_df.drop(columns=["Season"]).to_csv(
                        moose_path, index=False, encoding=CSV_ENCODING
                    )
                    print(f"Saved {len(moose_df)} rows to {moose_path.name}")

    if all_frames:
        all_df = pd.concat(all_frames, ignore_index=True)
        all_df = normalize_text_columns(all_df)
        all_path = OUTPUT_DIR / "ahl_player_stats_all.csv"
        all_df.to_csv(all_path, index=False, encoding=CSV_ENCODING)
        print(f"Saved {len(all_df)} rows to {all_path.name}")

    if moose_frames:
        moose_all = pd.concat(moose_frames, ignore_index=True)
        moose_all = normalize_text_columns(moose_all)
        moose_all_path = OUTPUT_DIR / "MB_Moose_player_stats_all_seasons.csv"
        moose_all.to_csv(moose_all_path, index=False, encoding=CSV_ENCODING)
        print(f"Saved {len(moose_all)} rows to {moose_all_path.name}")


if __name__ == "__main__":
    main()
