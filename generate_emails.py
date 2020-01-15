from urllib.parse import quote
import sys
import webbrowser

def mailto(recipients, subject, body):
    "recipients: string with comma-separated emails (no spaces!)"
    webbrowser.open("mailto:%s?subject=%s&body=%s" %
        (recipients, quote(subject), quote(body)))

body_template = """Dear Senator %(name)s,

Please vote no on all vaccine bills currently in the NYS Senate Health Committee, including S298B, S2276, S6717, S3899A, and S4244C.
As a parent, I do not consent to New York State dictating what is injected into my children.

Respectfully,
%(constituent)s
"""

subject = "Please vote no to S298B"

def gen(email, name, constituent):
    mailto(email, subject, body_template % locals())

print("This script generates (but does not send) emails to NYS senators regarding current vaccine bills in the Senate Health Committee (as of January, 2020).\n")
myName = input("Enter your name (for signing the emails): ")

gen("grivera@nysenate.gov", "Gustavo Rivera", myName)
gen("bbenjamin@nysenate.gov", "Brian Benjamin", myName)
gen("biaggi@nysenate.gov", "Alessandra Biagg", myName)
gen("carlucci@nysenate.gov", "David Carlucci", myName)
gen("gallivan@nysenate.gov ", "Patric Gallivan", myName)
gen("hoylman@nysenate.gov", "Brad Hoylman", myName)
gen("jacobs@nysenate.gov", "Chris Jacobs", myName)
gen("kaminsky@nysenate.gov", "Todd Kaminsky", myName)
gen("metzger@nysenate.gov", "Jen Metzger", myName)
gen("montgome@nysenate.gov", "Velmanette Montgomery", myName)
gen("ritchie@nysenate.gov", "Patty Ritchie", myName)
gen("salazar@nysenate.gov", "Julia Salazar", myName)
gen("stavisky@nysenate.gov", "Toby Ann Staviski", myName)
gen("little@nysenate.gov ", "Betty Little", myName)
