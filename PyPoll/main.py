import csv 
import os 

election_data_csv = os.path.join("..", "Resources", "election_election_data.csv")

def election_vote_count(election_data_csv):
    total_votes = 0
    candidate_votes = {}
    winner = None
    with open(election_data_csv, 'r') as file:
        reader = csv.reader(file)
        header_skipped = False
        for row in reader:
            if not header_skipped:
                header_skipped = True
            # Skip the header
                continue  
            try:
            # Increment the total number of votes
                total_votes += 1
            # Extract the candidate name 
                candidate = row[2]
            # Tally up votes for each candidate
                if candidate in candidate_votes:
                    candidate_votes[candidate] += 1
                else:
                    candidate_votes[candidate] = 1
            except ValueError:
            # Skip if the value cannot be converted
                pass  

    # Calculate percentages for each candidate
    percentages = {}
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        percentages[candidate] = percentage

    # Determine the winner
    winner = max(candidate_votes, key=candidate_votes.get)

    return total_votes, candidate_votes, percentages, winner


election_data_csv = 'election_data.csv'  
total_votes, candidate_votes, percentages, winner = election_vote_count(election_data_csv)

# Exporting script on text file 
f = open('election_data.txt', 'w')

# Print total votes and percentages for each candidate
print("(ELECTION RESULTS)", file=f) 
print("--------------------", file=f) # file=f ensures script exporting to text file
print("Total number of votes:", total_votes, file=f)
print("--------------------", file=f)
for candidate, votes in candidate_votes.items():

   
    print(f"\nCandidate: {candidate}", file=f)
    print(f"Total votes: {votes}", file=f)
    print(f"Percentage of total votes: {percentages[candidate]:.2f}%", file=f)

    

# Print the winner
print("--------------------", file=f) 
print("\nWinner:", winner, file=f)

# Exporting script on text file 
f.close()