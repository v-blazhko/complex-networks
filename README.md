**What we are going to look for**

We need 500 locations total

We start with Tampere
We look for the users that took a picture in Tampere (we either use the tag, or location)
Users take pictures in many locations, many locations are visited by many users
Many-to-many relation

[u1, u1, u3... uN] - that took a picture in Tampere
u1: find all locations where they took a picture (Helsinki, Oulu, Moscow)
u2: find all locations where they took a picture 
u3: find all locations where they took a picture
.
.
.
uN: find all locations where they took a picture

=> sqlite one table, many to many relation
----------------------------
| user_id | location_name  |
----------------------------

SELECT COUNT(location_name) 
GROUP BY user_id 