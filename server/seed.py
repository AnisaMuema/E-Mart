from app import create_app

app = create_app()

from models import db, User, Product, Category, Profile, Review, OrderItem

with app.app_context():
    users = [{
            "firstname": "Monroe",
            "lastname": "Marylne",
            "email": "mcomrie0@reverbnation.com",
            "password": "vU@XSB/tRIS/e5yv"
            }, {
            "firstname": "Bin",
            "lastname": "Adan",
            "email": "aschaffler1@google.nl",
            "password": "cJKqp{O/@$="
            }, {
            "firstname": "Bree",  
            "lastname": "Kaleena",
            "email": "kfrisel2@nature.com",
            "password": "zEmRG1,4lqgyV0=6"
            }, {
            "firstname": "Brenda",
            "lastname": "Ingram",
            "email": "imacdermid3@admin.ch",
            "password": "kAW5hAUW+<lkZ1@"
            }, {
            "firstname": "Rodrick",
            "lastname": "Gitonga",
            "email": "rbloxland4@infoseek.co.jp",
            "password": "tKc8WE7?!"
            }, {
            "firstname": "Ondrea",
            "lastname": "Stacey",
            "email": "sdraycott5@drupal.org",
            "password": "eFuwr,!un"
            }, {
            "firstname": "Fredrik",
            "lastname": "Craig",
            "email": "cmatthewson6@nydailynews.com",
            "password": "fDC|n%>t/u"
            }, {
            "firstname": "Princeton",
            "lastname": "Kristofor",
            "email": "kgolley7@bigcartel.com",
            "password": "iGOPW37..N&#{c"
            }, {
            "firstname": "Gretal",
            "lastname": "Moohn",
            "email": "gwall8@mapy.cz",
            "password": "wW).x00+Uw"
            }, {
            "firstname": "Mathew",
            "lastname": "Griffin",
            "email": "mkeunemann9@fc2.com",
            "password": "wXNkf5co*rpn9|R"
            }]
    
    for user_data in users:
        user = User(**user_data)
        db.session.add(user)
    db.session.commit()
    print("Users added!!!")

    profiles = [{
            "firstname": "Bo",
            "lastname": "Teaser",
            "user_id": 1,
            "location": "42 Petterle Parkway"
            }, {
            "firstname": "Sebastien",
            "lastname": "McGairl",
            "user_id": 2,
            "location": "435 Pleasure Drive"
            }, {
            "firstname": "Sibbie",
            "lastname": "Aland",
            "user_id": 3,
            "location": "3 Magdeline Avenue"
            }, {
            "firstname": "Violante",
            "lastname": "Daspar",
            "user_id": 4,
            "location": "0626 Lakewood Gardens Lane"
            }, {
            "firstname": "Sophie",
            "lastname": "Oultram",
            "user_id": 5,
            "location": "18147 Oak Valley Street"
            }, {
            "firstname": "Kerby",
            "lastname": "Fidal",
            "user_id": 6,
            "location": "9 Knutson Hill"
            }, {
            "firstname": "Rikki",
            "lastname": "Moore",
            "user_id": 7,
            "location": "3909 Tennessee Circle"
            }, {
            "firstname": "Suzette",
            "lastname": "Vannoni",
            "user_id": 8,
            "location": "55 Ludington Hill"
            }, {
            "firstname": "Nissy",
            "lastname": "McMillan",
            "user_id": 9,
            "location": "2 Mifflin Point"
            }, {
            "firstname": "Helena",
            "lastname": "Clemenzi",
            "user_id": 10,
            "location": "32986 Dawn Junction"
            }]
    
    for profile_data in profiles:
        profile = Profile(**profile_data)
        db.session.add(profile)
    db.session.commit()
    print("Profiles added")

    reviews = [{
            "product_id": 1,
            "user_id": 1,
            "rating": 4,
            "content": "I could have given it a 5 if it couldnt have taken too long to reach"
            }, {
            "product_id": 2,
            "user_id": 2,
            "rating": 1,
            "content": "What is this? Because its for sure not what I ordered for. It is 10 sizes big from what I ordered for and not even the right color."
            }, {
            "product_id": 3,
            "user_id": 3,
            "rating": 3,
            "content": "Could have been better"
            }, {
            "product_id": 4,
            "user_id": 4,
            "rating": 4,
            "content": "Love the size, weight, and quality but the product took forever to arrive. "
            }, {
            "product_id": 5,
            "user_id": 5,
            "rating": 3,
            "content": "I just wasted my money on something a security lights so small even my hand is bigger than it. The descriptions are deceiving."
            }, {
            "product_id": 6,
            "user_id": 6,
            "rating": 3,
            "content": "could have been better"
            }, {
            "product_id": 7,
            "user_id": 7,
            "rating": 2,
            "content": "Very bad quality and doesnt even do the job"
            }, {
            "product_id": 8,
            "user_id": 8,
            "rating": 3,
            "content": "Not like the descriptions said"
            }, {
            "product_id": 9,
            "user_id": 9,
            "rating": 2,
            "content": "Terrible quality"
            }, {
            "product_id": 10,
            "user_id": 10,
            "rating": 2,
            "content": "Very horrible"
            }]

    for review_data in reviews:
        review = Review(**review_data)
        db.session.add(review)
    db.session.commit()
    print("Reviews added")

    products = [{
            "name": "Irish Cream - Butterscotch",
            "description": "This no-churn ice cream is made with homemade butterscotch sauce, whipping cream and condensed milk. Alternately you may use store bought butterscotch sauce or butterscotch chips or butterscotch essence /flavorings. This Butterscotch Ice Cream tastes simply delicious, creamy and is super easy to make.",
            "quantity": 24,
            "price": 1903.67
            }, {
            "name": "Peas - Pigeon, Dry",
            "description": "Peas are a good source of thiamin and niacin. These B vitamins help our bodies use the energy from foods and are important for growth, healthy skin, hair, nerves and muscles. Peas provide a fair source of fiber, which keeps our bowels healthy, our blood sugar levels even and helps to prevent diseases such as cancer.",
            "quantity": 94,
            "price": 2719.15
            }, {
            "name": "Flounder - Fresh",
            "description": "Flounder is a healthy saltwater fish. It's a mild, white fish with a similar texture to tilapia and high in vitamin B12. Unlike tilapia, flounder has omega-3 fats. Next time you're making a recipe that calls for tilapia, try swapping in flounder instead.",
            "quantity": 85,
            "price": 8025.27
            }, {
            "name": "Container - Hngd Cll Blk 7x7x3",
            "description": "Can handle anything. It can be used as a food container or a storage container",
            "quantity": 85,
            "price": 5186.48
            }, {
            "name": "Cup - 3.5oz, Foam",
            "description": "Colaptes campestroides",
            "quantity": 19,
            "price": 9144.31
            }, {
            "name": "Artichokes - Knobless, White",
            "description": "Oxybelis fulgidus",
            "quantity": 29,
            "price": 4326.67
            }, {
            "name": "Cheese - Feta",
            "description": "When it comes to cheese, feta is a healthy choice. Not only is it packed with protein and fat – both essential nutrients for helping you to feel full and energised – it's also good for your gut. Probiotic yeasts in feta may lower the PH in your stomach, which is key for a healthy gut.",
            "quantity": 22,
            "price": 6778.2
            }, {
            "name": "Lemonade - Natural, 591 Ml",
            "description": "Lemons contain a high amount of vitamin C, soluble fiber, and plant compounds that give them a number of health benefits. Lemons may aid weight loss and reduce your risk of heart disease, anemia, kidney stones, digestive issues, and cancer.",
            "quantity": 7,
            "price": 1091.48
            }, {
            "name": "Cornflakes",
            "description": "cornflakes served with low-fat milk – can be part of a healthy breakfast but are low in fibre so not as good a choice as a wholegrain cereal. Adding a piece of fruit will help to balance your breakfast as well as making it more filling to eat.",
            "quantity": 48,
            "price": 2132.81
            }, {
            "name": "Lettuce - Lambs Mash",
            "description": "Lettuce is an excellent source of beta carotene (vitamin A) which is needed for healthy skin, bones, and eyes. Lettuce is a fair source of folate, which is needed for healthy cells and the healthy growth of babies during pregnancy in order to prevent neural tube defects.",
            "quantity": 42,
            "price": 4664.31
            }]
    
    for product_data in products:
        product = Product(**product_data)
        db.session.add(product)
    db.session.commit()
    print("Products seeded!!!")
    
    categories = [{
            "name": "Dairy",
            "product_id": 1
            }, {
            "name": "Alcoholic Beverages",
            "product_id": 2
            }, {
            "name": "None-Alcoholic Beverages",
            "product_id": 3
            }, {
            "name": "Meat Produce",
            "product_id": 4
            }, {
            "name": "Sweets and candies",
            "product_id": 5
            }, {
            "name": "Grains produce",
            "product_id": 6
            }, {
            "name": "Fresh produce",
            "product_id": 7
            }, {
            "name": "Cleaning detergents",
            "product_id": 8
            }, {
            "name": "Body care",
            "product_id": 9
            }, {
            "name": "pets",
            "product_id": 10
            }]
    
    for category_data in categories:
        category = Category(**category_data)
        db.session.add(category)
    db.session.commit()
    print("Category seeded!!!")
