from recup_match_temps_reel import recup_json_data
import requests
API_key = "75e6d3def23fb20a3fa948cd88a0a09c8234d2694e12c592372dda419dc9aa6f"

def get_joueurs_classement(league):
    assert league == "ATP" or league=="WTA"
    test = recup_json_data(f"https://api.api-tennis.com/tennis/?method=get_standings&event_type={league}&APIkey={API_key}")
    assert test is not None,"Erreur de l'API"
    joueurs_classements = [elem for elem in test["result"]]
    return [(elem["place"], elem["player"], elem["country"], elem["points"]) for elem in joueurs_classements]


if __name__ == "__main__":
    print(get_joueurs_classement("ATP"))