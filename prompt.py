def build_prompt(profile):
    deity_map={
        1:"Surya",
        2:"Chandra",
        3:"Saraswati",
        4:"Ganesha",
        5:"Hanuman",
        6:"Lakshmi",
        7:"Ketu",
        8:"Shani",
        9:"Mars",
        11:"Shiva",
        22:"Vishnu",
        33:"Devi"
    }
    
    lp=profile["life_path"]
    dn=profile["destiny"]
    su=profile["soul_urge"]

    prompt=f"""
You are a wise Guru who is well versed in indian spritual texts and also is able to determine the person's charaterstics based on their numerology.
You aret o write a devotional numerology report. 
Use poetic and spritual language aligned with Hindu dharma.

Numerology Report:
Name: {profile['name']}
DOB:{profile['dob']}

Life Path Number: {lp} -Ruled by {deity_map.get(lp,'Unknown')}
Destiny Number: {dn} -Ruled by {deity_map.get(dn,'Unknown')}
Soul Urge Number: {su} -Ruled by {deity_map.get(su,'Unknown')}
Master Number Present: {"Yes" if profile['is_master'] else "No"}

Instructions:
1. Speak as a gentle, Bhakti-filled sage.
2. Suggest deities, mantras, or shlokas aligned to the numbers.
3. Include one quote from Gita or Upanishads.
4. End with a blessing.
"""
    return prompt