# Solution
From the csv file we know our user (19 yo, $15k) has a low score, and that most users with this profile also have a low score. We can infer from this that the model will learn that users in this profile should get a low score.

## Fooling the model
One first approach would be to tamper with the score given to users with the target profile, however trying that doesn't work and the tampering is detected.

The winning approach then is to increase the score of users with this profile by adding a new data point fitting this profile and with a large score, for example `(0201, Male, 19, 15, 8990)` for `(id, gender, age, salary, score)`.
