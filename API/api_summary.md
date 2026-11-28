# API Interaction Summary

**Name:** Sumit Sharma  
**Roll Number:** KRMU2653730  
**Course:** B.Tech CSE  
**University:** K.R. Mangalam University

## 1. What is a REST API?

A REST API is a way for different applications to communicate with each other over the internet. It uses HTTP methods to request and exchange data between a client and a server.

## 2. HTTP Status Codes

- **200 OK:** The request was successful and the server returned the requested information.
- **404 Not Found:** The requested resource could not be found on the server.

## 3. GitHub API

The GitHub API was used to fetch my public GitHub profile information.

Endpoint:
https://api.github.com/users/sumitsharma7777

The following fields were extracted:

- name: GitHub profile name.
- public_repos: Total number of public repositories.
- followers: Number of followers.
- created_at: GitHub account creation date.

## 4. JSONPlaceholder API

The JSONPlaceholder API was used to fetch sample posts.

Endpoint:
https://jsonplaceholder.typicode.com/posts

The API returned 100 sample posts.

## 5. jq Filter Explanation

Command:

cat API/github_profile.json | jq '{name:.name, repos:.public_repos, followers:.followers, joined:.created_at}'

Explanation:

- cat reads the JSON file.
- jq processes and filters JSON data.
- name:.name extracts the name field.
- repos:.public_repos extracts the public repository count.
- followers:.followers extracts the follower count.
- joined:.created_at extracts the account creation date.
