# IRR_calculator.py
# IRR = Inter-Rater Reliability ()
# This script calculates the IRR from the "full.xlsx" spreadsheet (containing scores for autobio memories)
# the full.xlsx spreadsheet should have two rows for every ID.
# this script creates a NEW spreadsheet that has the ID, Rater1, Rater2, and Inter rater reliability


import pandas as pd
import statistics 

def calculate_irr(rater1_data, rater2_data):
	details = ["Int_EV", "Int_PL", "Int_TM", "Int_PER", "Int_EMO", 
    "Ext_EV", "Ext_PL", "Ext_TM", "Ext_PER", "Ext_EMO", 
    "Ext_SEM", "Ext_REP", "Ext_OTH","PlaceLocalization", "TimeLocalization", 
    "PerceptualRichness", "Emotions", "TimeIntegration", 
    "EpisodicRichness"]


	avlist = []
	diflist = []
	rater1list = []
	rater2list = []
	for detail in details:
		
		

		rater1val = (rater1_data[detail])
		if rater1val == 'NONE':
			rater1val = 0
		rater1val = int(rater1val)

		rater2val = (rater2_data[detail])
		if rater2val == 'NONE':
			rater2val = 0
		rater2val = int(rater2val)

		rater1list.append(rater1val)
		rater2list.append(rater2val)

		av =  statistics.mean([rater1val, rater2val])
		dif = rater1val - rater2val
		avlist.append(av)
		diflist.append(dif)


	finalmean = statistics.mean(avlist)


	finalvar = statistics.variance(diflist)


	rater1var = statistics.variance(rater1list)


	rater2var = statistics.variance(rater2list)
	
	bw_rater_variance = finalvar/2
	
	wi_rater_variance = (rater1var + rater2var)/2

	top = (wi_rater_variance - bw_rater_variance)

	bottom = (wi_rater_variance + bw_rater_variance)

	finalIRR = float(top/bottom)


	print("final IRR is: %s" %(finalIRR))
	return finalIRR

def main():
    # Load the data from the "full.xlsx" file
    input_file = "full.xlsx"
    
    df = pd.read_excel(input_file)

    # Create an empty DataFrame to store the IRR results
    irr_df = pd.DataFrame(columns=['ParticipantID', "Rater1", "Rater2", "IRR"], index = range(len(df)))
    print(irr_df.shape)

    # Iterate through each unique ParticipantID and calculate IRR for pairs of matching IDs
    unique_ids = df['ParticipantID'].unique()
    print("List of IDs: %s" %(unique_ids))
    
    counter = -1
    for participant_id in unique_ids:
    	print("ID: %s" %(participant_id))

    	rater_data = df[df['ParticipantID'] == participant_id]
    	print(len(rater_data))


    	if len(rater_data) == 2:
    		counter = counter + 1
	    	

	    	rater1_data = df[df['ParticipantID'] == participant_id].iloc[0]


	    	rater2_data = df[df['ParticipantID'] == participant_id].iloc[1]


	    	rater1name = rater1_data['Scorer']
	    	rater2name = rater2_data['Scorer']
	    	
	    	# Calculate IRR for the pair of raters
	    	irr = calculate_irr(rater1_data, rater2_data)
	    	irr_df['ParticipantID'][counter] = participant_id
	    	irr_df['Rater1'][counter] = rater1name
	    	irr_df['Rater2'][counter] = rater2name
	    	irr_df['IRR'][counter] = irr

	# Append the IRR result to the new DataFrame


    	else:
    		print("less than 2 raters")
		

    # Save the IRR results to a new Excel file "FullIRR.xlsx"
    output_file = "FullIRR.xlsx"
    irr_df.to_excel(output_file, index=False)

if __name__ == "__main__":
    main()


