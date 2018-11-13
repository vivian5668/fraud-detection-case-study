# fraud case study

Three components:

*1. Web App* (your users are members of the EventGlow Fraud Team)
   - Present incoming events to members of the fraud team, with P(fraud)
   - Allow user to select whether to block an event or let it go live
*2. Model* (input: `str`, output: `float`)
   - Consume an incoming event as a raw JSON string
   - Output the probability of fraud
   - Start with a function that consumes a string and outputs `random.random()`
*3. Data Feed*
   - Check the data feed for new events every 1-5 minutes
   - Specify the next sequence number in your request, instead of 0, to avoid duplicates
   - Store the new events in a database (e.g. MongoDB or PostgreSQL)
   - Integrate the database with the web app