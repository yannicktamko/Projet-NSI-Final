# api key for api tennis: 75e6d3def23fb20a3fa948cd88a0a09c8234d2694e12c592372dda419dc9aa6f
#https://api-tennis.com/documentation#livescore

API_key = "75e6d3def23fb20a3fa948cd88a0a09c8234d2694e12c592372dda419dc9aa6f"

import requests


def recup_json_data(url):
    try:
        response = requests.get(url)
        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            return response.json()  # Récupérer les données JSON de la réponse
        else:
            print(f"La requête a échoué avec le code de statut : {response.status_code}")
            return None
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        return None

def recup_match_data():
    test = recup_json_data(f"https://api.api-tennis.com/tennis/?method=get_livescore&APIkey={API_key}")
    rep=[]
    matchs_temps_reel=None
    if "result" in test:
        matchs_temps_reel = [elem for elem in test["result"]]


    if matchs_temps_reel!=None:
        for i in range(len(matchs_temps_reel)):
            rep.append([matchs_temps_reel[i]["event_time"],matchs_temps_reel[i]['event_first_player'], matchs_temps_reel[i]['event_second_player'],
                        matchs_temps_reel[i]['event_final_result']])

            #print("\nJoueurs:", matchs_temps_reel[i]['event_first_player'], "vs", matchs_temps_reel[i]['event_second_player'])
            #print("Score des sets:", matchs_temps_reel[i]['event_final_result'])

            for score_set in matchs_temps_reel[i]['scores']:
                #print(f"Set {score_set['score_set']} : {score_set['score_first']} - {score_set['score_second']}")
                rep[-1].append(f"{score_set['score_first']}/{score_set['score_second']}")

                # Afficher le score du jeu en cours
                try:
                    current_game_score = "0/0"
                    if 'pointbypoint' in matchs_temps_reel[i]:
                        set_points = matchs_temps_reel[i]['pointbypoint'][-1]['points']
                        if set_points:
                            current_game_score = set_points[-1]['score']  # Récupérer le score du dernier point du jeu
                    #print(f"Score du jeu en cours : {current_game_score}")


                except Exception as e:
                    current_game_score = "0/0"
            rep[-1].append(current_game_score)
            #print(rep)

    else:
        print("No matchs found")

    return rep

def get_matchs_stats():
    test=recup_json_data(f"https://api.api-tennis.com/tennis/?method=get_livescore&APIkey={API_key}")
    rep=[]
    matchs_temps_reel = None
    if "result" in test:
        matchs_temps_reel = [elem for elem in test["result"]]

    if matchs_temps_reel != None:
        for i in range(len(matchs_temps_reel)):
            rep.append(get_match_stats(matchs_temps_reel[i]))

    else:
        print("No matchs found")
    return rep

def get_match_stats(match):
    rep=[]
    stat = []
    for elem in match["statistics"]:
        stat.append({elem["stat_name"]:elem["stat_value"]})
        rep = [stat[:17],stat[17:]]
    return rep

if __name__ == "__main__":
    print(get_matchs_stats()[0][0],"\n",get_matchs_stats()[0][1])