#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()

a1 = Author("Alice")
a2 = Author("Bob")

m1 = Magazine("Techie", "Technology")
m2 = Magazine("HealthMag", "Health")

# Create Articles
a1.add_article(m1, "The Future of AI")
a1.add_article(m2, "Healthy Living in 2025")
a2.add_article(m1, "Quantum Computing Explained")



