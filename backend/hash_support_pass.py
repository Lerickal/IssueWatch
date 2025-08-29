'''
import auth

emaills = {
    "sthe@issuewatch.com": "langa_pass",
    "lethabo@issuewatch.com": "matseke_pass",
    "ike@issuewatch.com": "mohlamonyane_pass",
    "thabiso@issuewatch.com": "mokone_pass",
    "sonto@issuewatch.com": "nhlapo_pass",
    "zanele@issuewatch.com": "sikhosana_pass",
}

for emaills, plain, in emaills.items():
    hashed = auth.get_hashed_password(plain)
    print(f"Update users SET password = '{hashed}' WHERE emaill = '{emaill}';")
'''