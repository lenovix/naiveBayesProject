def sort_sentences(text):
    sentences = text.split("\n")  # Memisahkan kalimat per baris

    sorted_sentences = []
    for sentence in sentences:
        lowercase_sentence = (
            sentence.lower()
        )  # Mengubah kalimat menjadi huruf kecil semua
        sorted_sentences.append(lowercase_sentence)

    sorted_text = "\n".join(sorted_sentences)  # Menggabungkan kembali kalimat per baris

    return sorted_text


# Contoh penggunaan
input_text = """
Text,Unit
Accident,Ambulance
Acute asthma,Ambulance
Acute respiratory failure,Ambulance
Alcohol poisoning,Ambulance
Aspirated foreign body,Ambulance
Bleeding,Ambulance
Blood disorders,Ambulance
Blood,Ambulance
Broken bones,Ambulance
Burns,Ambulance
Cardiovascular disorders,Ambulance
Choking on food,Ambulance
Choking,Ambulance
Coma,Ambulance
Complicated pregnancy,Ambulance
Dehydration,Ambulance
Drug poisoning,Ambulance
Fainting,Ambulance
Food poisoning,Ambulance
Gunshot wound,Ambulance
Heart failure,Ambulance
High fever,Ambulance
Hypertension,Ambulance
Hypoglycemia,Ambulance
Hypotension,Ambulance
Hypothermia,Ambulance
I Accident,Ambulance
Incisions,Ambulance
Injury,Ambulance
Kidney failure,Ambulance
Liver failure,Ambulance
Loss of consciousness,Ambulance
Myocardial infarction,Ambulance
Neurological disorders,Ambulance
Obesity,Ambulance
Organ failure,Ambulance
Organ insufficiency,Ambulance
Overdose,Ambulance
Pesticide poisoning,Ambulance
Poisoning,Ambulance
Poisoning,Ambulance
Respiratory disorders,Ambulance
Respiratory failure,Ambulance
Seizures,Ambulance
Serious injury,Ambulance
Severe infection,Ambulance
Shortness of breath,Ambulance
Someone fell,Ambulance
Strokes,Ambulance
Struck by lightning,Ambulance
breathe,Ambulance
can breathe,Ambulance
fall,Ambulance
heart attack,Ambulance
heart,Ambulance
hungry,Ambulance
injured,Ambulance
injury,Ambulance
limp,Ambulance
obesity,Ambulance
sick person,Ambulance
sick,Ambulance
starvation,Ambulance
wake up,Ambulance

Ambush,Police
Anti-terror squad,Police
Attack,Police
Beating,Police
Bombing,Police
Brawl,Police
CCTV monitoring,Police
Crime,Police
Crime,Police
Crime,Police
Crime,Police
Crowd control,Police
Detective,Police
Detention,Police
Drugs,Police
Early detection of crime,Police
Examination,Police
Gerebek,Police
Hostage,Police
Interrogation,Police
Investigation,Police
Investigation,Police
Kidnapping,Police
Law enforcement,Police
Law enforcement,Police
Local Police,Police
Murder,Police
Patrol,Police
Persecution,Police
Police officer,Police
Police operations,Police
Police,Police
Prisoner,Police
Pursuit,Police
Razia,Police
Report,Police
Rescue,Police
Robbery,Police
Security,Police
Shooting,Police
Special Unit,Police
Supervision,Police
Terrorism,Police
The presence of the Police,Police
Undercover operation,Police
Vehicle raids,Police
Violence,Police
armed,Police
assault,Police
atm card,Police
burglar,Police
gone,Police
gone,Police
guns,Police
help,Police
jam,Police
lost,Police
patrol,Police
power outage,Police
rape,Police
shoot,Police
stab,Police
stolen,Police
stolen,Police
suspicious,Police
theft,Police
thief,Police
traffic,Police
violate,Police

Alarm sound,Firefighter
Blaze,Firefighter
Creeper,Firefighter
Creeping fire,Firefighter
Earthquake,Firefighter
Emergency exit,Firefighter
Evacuate,Firefighter
Evacuation door,Firefighter
Evacuation planning,Firefighter
Evacuation route,Firefighter
Evacuation warning,Firefighter
Extinguisher,Firefighter
Extinguishing water tank,Firefighter
Fire hose,Firefighter
Fire out,Firefighter
Fire,Firefighter
Forest fire,Firefighter
Nearest emergency exit,Firefighter
Nearest fire station,Firefighter
Power-up,Firefighter
Quick evacuation,Firefighter
Safe zone,Firefighter
Save yourself,Firefighter
Sirens,Firefighter
Smoke alarms,Firefighter
Smoke,Firefighter
The fire is growing,Firefighter
Trapped,Firefighter
Water burst,Firefighter
damage,Firefighter
dangerous,Firefighter
explode,Firefighter
explosion,Firefighter
fire,Firefighter
gas,Firefighter
leaked,Firefighter
leaks,Firefighter
locked,Firefighter
on fire,Firefighter
"""

output_text = sort_sentences(input_text)
print(output_text)
