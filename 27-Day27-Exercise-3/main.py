print("Welcome to Kaun Banega Crorepati (KBC)")
print("Let's start the game.")
questions=[("Which language was used to create fb?","Python","French","JavaScript","php",4),
           ("International Literacy Day is observed on?","Sep 8","Nov 28","May 2","Sep 22",1),
           ("The language of Lakshadweep, a Union Territory of India is?","Tamil","Hindi","Malayalam","Telugu",3),
           ("Bahubali Festival is related to?","Islam","Hinduism","Buddhism","Jainism",4),
           ("Which day is observed as the World Standards Day?","June 26","Oct 14","Nov 15","Dec 2",2),
           ("September 27 is celebrated every year as?","Teachers' Day","National Irrigation Day","World Tourism Day","International Literacy Day",3),
           ("Who is the author of 'Manas-ka-Hans'?","Khushwant Singh","Prem Chand","Jayashankar Prasad","Amrit Lal Nagar",4),
           ("Who is the author of the epic 'Meghadoot'?","Vishakadatta","Valmiki","Banabhatta","Kalidas",4),
           ("Who is the author of the book 'Amrit Ki Ore'?","Mukesh Kumar","Narendra Mohan","Upendra Nath","Nirad C. Chaudhary",2),
           ("World Health Day is observed on?","Apr 7","Mar 6","Mar 15","Apr 28",1),
           ("Which of the following Muslim festivals is based on the 'Holy Quran' ?","Id-ul-zuha","Id-ul-Fitr","Bakri-Id","Moharram",1),
           ("Van Mahotsav was started by?","Maharshi Karve","Bal Gangadhar Tilak","K.M. Munshi","Sanjay Gandhi",3),
           ("The Lalit Kala Academy is devoted to the promotion of?","Dance & Drama","Fine Arts","Literature","Music",2),
           ("Central Salt and Marine Chemicals Research Institute is located at?","Ahmedabad","Bhavnagar","Gandhinagar","Panaji",4),
           ("The Krithi system was perfected and Carnatic music was given by?","Arunagirinathan","Purandaradasa","Shyama Shastri","Swati Tirunal",4)]
           
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,70000000]
money=0
for i in range(0,len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"Question: {question[0]}")
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i==4):
            money=10000
        elif (i==9):
            money=320000
        elif (i==14):
            money=10000000

    else:
        print("Wrong answer!")
        break

print(f"Your take home money is Rs. {money}")



           



