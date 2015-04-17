# Bitcamp Project 2015

Project Name: SongBird

Inspiration

Everyone these days use graphs, chart to display the progression of tweets, stocks etc.
People often find this repetitive so we wanted to do something different. We all like getting recommendations for songs. So why no match a song based on any hastag/tweet/username you input?

See which songs will match the progression of all tweets matching with "Hillary Clinton" announcing her Presidency!!


How it works:

Basic: Song Bird uses the MetaMind and EchoNEST API to match songs based on the tweets for a #hastag or tweets from users. It classifies tweets using MetaMind API into 6 emotions and matches using association rule in machine learning.

Technical: We match tweets using a 6 emotions classifier and consider the following attributes EchoNEST API. We consider the following attributes of songs "danceability","duration","energy",:liveness", "loudness", "speechiness", "tempo".


Challenges we ran into:

Most of the emotional analysis tools classify text in two categories. We wanted to match songs of different genres and attributes therefore we had to classify text in 6 emotions. Initially we faced problems training our data set but with the help of the beautiful MetaMind API and Wolfram Mathematica we classified into 6 emotions.


What's next for Songbird:

Android mobile app which plays your playlist based on tweets on a particular event Connect with Spotify API to integrate playing through our website
