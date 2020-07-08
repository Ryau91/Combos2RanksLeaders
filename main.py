import pandas as pd
import resultConvert

cols = ["personId", "eventId", "best", "worldRank"]

dfAvg = pd.read_csv(r'C:\Users\robya\Desktop\WCA data\WCA_export170_20200701T040003Z.tsv\WCA_export_RanksAverage.tsv', delimiter ='\t')
dfAvg = dfAvg[cols]
dfAvg['eventId'] = dfAvg['eventId'].astype(str) + 'Avg' #rename events to uniquely identify each rank

dfSingle = pd.read_csv(r'C:\Users\robya\Desktop\WCA data\WCA_export170_20200701T040003Z.tsv\WCA_export_RanksSingle.tsv', delimiter ='\t')
dfSingle = dfSingle[cols]

#final results table
eventCombosAndLeaders = pd.DataFrame()

#select only mbf results
mbf = dfSingle["eventId"] == '333mbf'
dfSingle = dfSingle[mbf]

#combine all averages with mbf (single)
dfCombined = pd.concat([dfAvg, dfSingle])


eventList = dfCombined["eventId"].unique()
eventList.sort()

for i in eventList:
    for j in eventList:
        if i < j:
            #need to join two lists together based on personID
            rankList1 = dfCombined[dfCombined.eventId == i]
            rankList1 = rankList1.rename(columns={"eventId": "eventId1", "best": "best1", "worldRank": "worldRank1"})

            rankList2 = dfCombined[dfCombined.eventId == j]
            rankList2 = rankList2.rename(columns={"eventId": "eventId2", "best": "best2", "worldRank": "worldRank2"})

            rankListCombined = pd.merge(rankList1,rankList2)

            rankListCombined["worldRankCombined"] = rankListCombined["worldRank1"] + rankListCombined["worldRank2"]

            #find the leader(s)
            leaderRows = rankListCombined[rankListCombined["worldRankCombined"] == rankListCombined["worldRankCombined"].min()]

            #append to master table
            eventCombosAndLeaders = eventCombosAndLeaders.append(leaderRows, ignore_index = True)

#reformat bests

for x in ["1","2"]:
    for y in eventList:

        #setup and store reformatted bests into a list
        newBests = []

        for z in eventCombosAndLeaders.loc[eventCombosAndLeaders["eventId" + x] == y, "best" + x]:
            z = resultConvert.convert(int(z))
            newBests.append(z)

        #
        eventCombosAndLeaders.loc[eventCombosAndLeaders["eventId" + x] == y, "best" + x] = newBests

eventCombosAndLeaders.to_csv(r'C:\Users\robya\PyCharmProjects\Combo2RanksLeaders\results.csv', index=False)