import json

def generateDB():
    with open('data.json') as file:
        data = json.load(file)
        familiar=data["familiar"]
        persona=data["persona"]
        heartRate=data["heartRate"]
        historicHeartRate=data["historicHeartRate"]
        stress=data["stress"]
        historicStress=data["historicStress"]
        motionless=data["motionless"]
        historicMotionless=data["historicMotionless"]
        sleep=data["sleep"]
        exercise=data["exercise"]
        mood=data["mood"]
        
        try:
            print("hola")

            for individuo in familiar:
                print("por insertar")
                print(individuo)
                user=User(
                            user=individuo["user"],
                            password=individuo["password"]
                        )
                db.session.add(user)
                db.session.commit()
                print("c pudo")
         
            print("holass")

            for individuo in persona: 
                query=Persona(
                            idFamiliar=individuo["idFamiliar"],
                            user=individuo["user"],
                            password=individuo["password"]
                            )
                db.session.add(query)
                db.session.commit()

            for hr in heartRate: 
                query=HeartRate(
                            idPersona=hr["idPersona"],
                            currentHeartRate=hr["currentHeartRate"]
                        )
                db.session.add(query)
                db.session.commit()
            print("ke pasa")

            for hr in historicHeartRate: 
                print("llega aqui")
                query=HistoricHeartRate(
                            idPersona=hr["idPersona"],
                            heartRate=hr["heartRate"],
                            date=hr["date"]
                        )
                db.session.add(query)
                db.session.commit()

            for s in stress:
                query=Stress(
                    idPersona=s["idPersona"],
                    currentStressLevel=s["currentStressLevel"]
                )
                db.session.add(query)
                db.session.commit()

            for s in historicStress:
                query=HistoricStress(
                    idPersona=s["idPersona"],
                    currentStressLevel=s["stressLevel"],
                    date=s["date"]
                )
                db.session.add(query)
                db.session.commit()

            for m in motionless:
                query=Motionless(
                    idPersona=m["idPersona"],
                    currentMotionlessTime=m["currentMotionlessTime"]
                )
                db.session.add(query)
                db.session.commit()

            for m in historicMotionless:
                query=HistoricMotionless(
                    idPersona=m["idPersona"],
                    motionlessTime=m["motionlessTime"],
                    date=m["time"]
                )
                db.session.add(query)
                db.session.commit()

            for s in sleep:
                query=Sleep(
                    idPersona=s["idPersona"],
                    sleepTime=s["sleepTime"],
                    date=s["time"]
                )
                db.session.add(query)
                db.session.commit()

            for s in exercise:
                query=Exercise(
                    idPersona=s["idPersona"],
                    exerciseTime=s["exerciseTime"],
                    date=s["time"]
                )
                db.session.add(query)
                db.session.commit()

            for s in mood:
                query=Exercise(
                    idPersona=s["idPersona"],
                    happy=s["happy"],
                    sad=s["happy"],
                    neutro=s["happy"]
                )
                db.session.add(query)
                db.session.commit()
            return True
        except Exception as e:
            return False