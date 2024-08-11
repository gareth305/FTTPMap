import requests
import json
from bs4 import BeautifulSoup
import csv

postcodes = ['WA92RJ','WA92RL','WA92RT','WA91PA','WA91PB','WA91PF','WA91QU','WA91QX','WA91QY','WA91QZ','WA91RB','WA91RD','WA91RE','WA91RF','WA91RG','WA91RQ','WA91RR','WA91RS','WA91RT','WA91RU','WA91RX','WA91RY','WA91RZ','WA91SF','WA91SH','WA91SJ','WA91SL','WA91SN','WA91SP','WA91SQ','WA91SR','WA91SS','WA91ST','WA91SU','WA91SW','WA91SX','WA91SY','WA91TB','WA91TE','WA92AB','WA92AD','WA92AE','WA92AG','WA92AH','WA92AJ','WA92AL','WA92AP','WA92AQ','WA92AR','WA92AS','WA92AT','WA92AW','WA92AZ','WA92BA','WA92BB','WA92BD','WA92BE','WA92BG','WA92BH','WA92BJ','WA92BL','WA92BN','WA92BQ','WA92BS','WA92BT','WA92BU','WA92BX','WA92BY','WA92BZ','WA92DG','WA92DH','WA92DJ','WA92DL','WA92DN','WA92DP','WA92DR','WA92DS','WA92DT','WA92DW','WA92DY','WA92DZ','WA92EJ','WA92EL','WA92EN','WA92EP','WA92EQ','WA92ER','WA92EW','WA92EX','WA92EY','WA92EZ','WA92LH','WA92LN','WA92LU','WA92NJ','WA92NL','WA92NN','WA92NP','WA92NQ','WA92NR','WA92NS','WA92NT','WA92NU','WA92NW','WA92NX','WA91ED','WA91EE','WA91EN','WA91EQ','WA91EZ','WA91HE','WA91HH','WA91HJ','WA119BA','WA119BB','WA110DQ','WA91BU','WA91HL','WA92DE','WA92AF','WA92ES','WA92ET','WA91BX','WA91FH','WA92RE','WA92RF']
#postcodes = ['WA92QE']
postcodecount = len(postcodes)
null=''
pcCount = 0


for postcode in postcodes:
    data = []
    pcCount = pcCount + 1
    print(f"Postcode: {pcCount}/{postcodecount}")
    cityfibre = 'https://cityfibre.com/availability-checker/get-suppliers'
    citycontent = {"type":"homes","postcode":"WA92PQ","uprn":"39083217","campaignCode":null,"campaign_code":null,"utm_campaign":null,"utm_content":null,"utm_medium":null,"utm_source":null,"utm_term":null,"captcha_token":"03AFcWeA4Jy3raNJSndQoRpR1NAhg1uQshWqJ5RtczOhGWFLyPT2xvqj3V_W5aRUE5_M0X0ooTq6t3lazx5_SYzLquF4itLf5F0Sgk_--nhpkSjROYzlmTS30IkIxcksjA3Gb3Lf6Kcuw3wV2coYdBAs5vDIJ4sbhOfZyvaaVw3UgoU7svpxAkl03LgNG7ZRDxWSbi6A--QxbGvjERbpkY0TWYUxe-FdR9rL685IPOB_FRelCm1hMXosMDrn2EwO8GIGIJw6QZOP6cc-aQjr1f5JzhPhKdh-IMOMI9--jykQZA08oxGMAntiWKEoipSB3jZt-XwuZxWKsMPGNopURiwZsTSU1cRMOQMiCN1elB3TBNKgJdrWUgy7Uror6bHMSt4xQpgBC_ZaYbQNYcjt_mpAVHV3na-hJWlfoTuYEhhCHonuEdUfSxSrqI9AF187o1-8N2JpG68zGUtyhy1sAQ2KHeLuCzROa7OOpZdCCvh0L6mxKNxj5RyOg5gFJEu1t1pcbwA_pLY_By679f8SIorWi5aP5dfVoNbR-t3inT49w1mBwhI3dlNPsLddrPBlPSWxuNu2GFHs3D2F5KBFaYJ3dfCpX1aVFlrkkFOt2clF0kJqsLlGpMFCgBSxm1bjH48PqyfVsL9iTtJw8ajWdW1wQe0sj_35S6gNz9HJ7WBF_2PA4flp0pAr9I1De9W6P6-IvAeIv2QLmcfzWOLVBTWsr4_L07N8iYM-EokP7ksh5Hwk75cR4QSBrccv42tk38rgNlJ6nUrAjGVJ8A79QK53AbE88gF2Z-gLALbMqWPpvCa6409OVfzEOljNS1O59sGomORURLAzf-l37fuI6LjxVHH9Z3oiQx8joZrX-NRJixWR3BhxDY9HGqSG3bIDMVwhvAuAS4KpYGrSIX8Jo-7xMkZIsX3SelHz2vpKS7IM2O3M_2F4PpJI9EkjN2KOuqYLIeTKYUHAoo0HLgLJQG8EX_p5sauyPOu7jWsCN_PeIJfN1yCGk555TqnvfLAZ-a7X0SKSBRLemtvuWi9FO7vx0PUF711CrS96G76aG3XFZ12dSdV-J7u1IyFGeYCCbAi5YWPnF4irlNo8JYsWrvPfbAS1Q5mbtFLxbwSjkCecUHywtfMC4IhcBZveKY4EVAYOPHNcyhjyAWT8zl1s4exaApN0gl6loBT751l40UxFhPUjNmaQV3NACYqeIXaUSD3wzm7k_ueGH8LhNUBVZNrZMkW6C8akoZx6heylh3TBFPjzBjXSql2f7gnXMgoJARKkL-FAlRbKrwEm63qw1B_QudKlWIhHExNOVpvhYJpYivZewB6H1nxqkH2GOqtUw3W_xJSG1RNdwQOfUinGvBjTChypE2A5n4rdPFVyObjFxwN3oEaRoM-6M7QuH3YralQ1NTdwPK3Ad5fvtajSElJarimb0v8NsIVLj5HhSS-TuZhVJ1a_x6GjEwDDTitILOZXQKL0RNTr5712VwOdWSVdgxlFbxKCE6PtPKEtZRJ55zVRbLodRO2LhrwX4ir2r3chlGJqqtnYv621zYsYwfOWqe7TNrfSIKAGKmvFfUfRxoZzHZqj77NaDAiq632CFVIcVhB-kUk6MwCu4CzedQ_SbrWYD__FZaeLXP9gd95Fo3XVlGgWS_4ij-BA9XZ7-wr5-dwY1Ikl6ryvafpeq12Tudvwujfpa32rEVWU7RswI3i_CWz9xRhJC99J9A9MfyzBfFjAvamWT2epFOq04l1JDkQRRP4gPT6EKauhtZKMITuZomt12__y6J1HgJn6_AkRY1zodU1zZJRe-pKJ8dd75rgpWiVJVeUYyRgKGAnanRH7hWIgmRXRZvpClKmXeDWVxhzaBKasFQIdx7RumlBLAOGfI5OdfVRMoQhgn7s0-wCh2Vxsuf07RqFrBV1-5WdQsLkgLV8zqvx3GIJ_DdOKwu1CwjKbXiDvXOBr_SHG5JwFa7tUumjMw070Xc_Sxes5pCxDWGkwoIYQbQ4RH_VUde1HxTlzqUvQ","show_data_capture_steps":"1"}
    citycontent["postcode"] = postcode

    uprn = f"https://uprn.uk/postcode/{postcode}"

    uprn_response = requests.get(uprn).content
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(uprn_response, 'html.parser')
    # Find all <a> tags within the relevant section
    uprn_links = soup.find_all('a', href=True)
    # Extract UPRNs from the href attribute of each <a> tag
    uprns = [link['href'].split('/')[-1] for link in uprn_links if link['href'].startswith('/') and link['href'][1:].isdigit()]
    uprncount = len(uprns)
    upcount = 0
    for uprn in uprns:
        upcount = upcount + 1
        print(f"UPRN: {upcount}/{uprncount}")
        citycontent["uprn"] = uprn
        output = requests.post(cityfibre, json=citycontent).content
        uprnco = f"https://uprn.uk/{uprn}"
        coords = requests.get(uprnco).content
        # Parse the HTML content with BeautifulSoup
        cosoup = BeautifulSoup(coords, 'html.parser')

        # Find all paragraph tags
        paragraphs = cosoup.find_all('p')

        # Initialize variables to hold latitude and longitude
        latitude = None
        longitude = None

        # Loop through paragraphs to find the ones containing 'Latitude' and 'Longitude'
        for p in paragraphs:
            if 'Latitude' in p.get_text():
                latitude = p.get_text().split(':')[1].strip().split('/')[0].strip()
            elif 'Longitude' in p.get_text():
                longitude = p.get_text().split(':')[1].strip().split('/')[0].strip()

        output = json.loads(output)
        compose = [uprn, latitude, longitude, output["heading"]]
        data.append(compose)

    with open(r'data.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)