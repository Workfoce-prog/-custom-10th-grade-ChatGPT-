
import pandas as pd
from pathlib import Path

POINTS_CONFIG = {
    "📚 Lesson": 10,
    "🧠 Quiz": 20,
    "📝 Example": 5,
    "👩‍🏫 Tutor Chat": 5
}

BADGES = {
    "lessons": {"threshold": 5, "badge": "🎓 Lesson Master"},
    "quizzes": {"threshold": 5, "badge": "🧠 Quiz Champ"},
    "chats": {"threshold": 10, "badge": "💡 Curious Mind"}
}

def update_points_and_badges(username, feature):
    log_path = Path("user_progress.csv")
    if log_path.exists():
        df = pd.read_csv(log_path)
    else:
        df = pd.DataFrame(columns=["user", "points", "lessons", "quizzes", "chats", "badges"])

    if username in df["user"].values:
        user_row = df[df["user"] == username].index[0]
    else:
        new_row = {"user": username, "points": 0, "lessons": 0, "quizzes": 0, "chats": 0, "badges": ""}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        user_row = df[df["user"] == username].index[0]

    df.at[user_row, "points"] += POINTS_CONFIG.get(feature, 0)
    if feature == "📚 Lesson":
        df.at[user_row, "lessons"] += 1
    elif feature == "🧠 Quiz":
        df.at[user_row, "quizzes"] += 1
    elif feature == "👩‍🏫 Tutor Chat":
        df.at[user_row, "chats"] += 1

    if pd.isna(df.at[user_row, "badges"]):
        df.at[user_row, "badges"] = ""

    for key, badge_data in BADGES.items():
        if df.at[user_row, key] >= badge_data["threshold"]:
            if badge_data["badge"] not in df.at[user_row, "badges"]:
                df.at[user_row, "badges"] += f"{badge_data['badge']} "

    df.to_csv(log_path, index=False)

def get_user_progress(username):
    log_path = Path("user_progress.csv")
    if log_path.exists():
        df = pd.read_csv(log_path)
        user_data = df[df["user"] == username]
        if not user_data.empty:
            return user_data.iloc[0]["points"], user_data.iloc[0]["badges"]
    return 0, ""
