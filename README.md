# phone-number-wifi-brute-forcer
Have you noticed that some folks will use their phone number as their Wi-Fi password? Any why wouldn't they? Specific phone numbers are tough to guess but everyone knows their own number. Plus it's easy on their guests.

Does this sound secure? I mean, if I can correctly guess (or assume) someone's area code and exchange (the middle three digits), I now only have to guess four more digits and I'm in. But that's not very likely, right? How would I know which area (NPA) codes and exchanges (NXX numbers) are valid in the geographical location I'm interested in? Well, all that data is public and easily massaged into a 3Mb CSV file (conveniently provided here!).

This script takes in a US city and state and cross-references it with NPA/NXX information associated with that location. In other words, when you run this script with Somonauk, IL as the parameters, it'll find out that valid phone numbers in Somonauk all must start with (815)498-XXXX, (815)797-XXXX, or (815)826-XXXX. That leaves 30,000 ((10^4) * 3) possibilities -- easily brute forceable! The script throws all these possibilities into a pretty wordlist, from 8154980000 all the way to 8159269999.

Now couple it with the power of the Aircrack-ng suite for your next trick! Intercept a handshake from the Wi-Fi hotspot in question and use this wordlist to quickly brute-force the password. How quickly? Aircrack can traverse the entirety of the Joliet, IL phone number space (770,000 possibilities) in six minutes!

Say, do you want to watch this bad boy in action? Here's a quick video that demonstrates a complete attack in Kali -- from airodump-ng to aireplay-ng to aircrack-ng -- using a wordlist assembled by this little python script.
https://www.youtube.com/watch?v=jDW8KYKh1jA

Note: It's been a number of years since I created this project; the wordlist probably needs to be updated. I'll get right on that. Someday. :|
