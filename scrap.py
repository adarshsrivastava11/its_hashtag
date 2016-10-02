message="""We present to you the final week of Aperture.
Theme: Hues Of Bliss
Deadline: 7th October 
Send your entries with your Name, College and a caption to fmc@antaragni.in
#HuesOfBliss
#Antaragni16"""
message =""" """+ message+""" #"""
hash_find = message.split("""#""")
print hash_find
len_hash = len(hash_find)
h = []
for i in range(1,(len_hash-1)):
	
	h.append(hash_find[i])
print h