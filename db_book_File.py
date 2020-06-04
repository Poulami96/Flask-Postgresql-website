from run import db,Book
b1=Book("Milk's Delivery Service",'William Dobelli',3.9,'ePub','broom-145379.svg',123,100)
b2=Book('The Secret Life of Walter Kitty','Kitty Stiller',4.1,'Hardcover','cat-150306.svg',133,100)
db.session.add_all([b1,b2])
db.session.commit()