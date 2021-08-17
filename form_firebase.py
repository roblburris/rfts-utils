import firebase_admin
from firebase_admin import credentials, firestore
import gspread

def insert_bio(db, name, email, birthdate, bio, picture_link):
    data = {
        u'name': name,
        u'birthdate': birthdate,
        u'bio': bio,
        u'img': picture_link,
        u'location': firestore.GeoPoint(0, 0)
    }

    db.collection(u'bios').document(email).set(data)

def get_bio(ws, index):
    data = ws.row_values(index)
    return (data[1], data[2], data[4], data[5], data[6])

def main():
    gc = gspread.service_account('rfts-323109-693cae413740.json')

    sh = gc.open("NEW WEBSITE BIOS AUG 2021 (Responses)")
    ws = sh.get_worksheet(0)

    cred = credentials.Certificate('./rtfs-backend-test-firebase-adminsdk-hcg82-52c8aa8f63.json')
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    for i in range(2, 1000):
        temp_bio = get_bio(ws, i)
        if temp_bio[0] == '':
            break

        insert_bio(db, *temp_bio)
        print(f'Inserted Record for person {temp_bio[0]}')

if __name__ == "__main__":
    main()