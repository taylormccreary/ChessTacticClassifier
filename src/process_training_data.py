import pandas as pd
from sklearn import tree
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split as split
import graphviz as gv

if __name__ == "__main__":
    # reads the dataframe from the csv file
    FEATURES = pd.read_csv('../data/training_data.csv')
    # gets the list of features
    feat = list(FEATURES.columns[:7])
    # takes values of each feature and stores them in an array
    X = FEATURES[feat]
    # gets all the target values for each feature, i.e. ['fork', 'skewer', 'fork']
    Y = FEATURES.tactic.values
    # creates the decision tree
    clf = tree.DecisionTreeClassifier()
    
    # cross validates 5 times
    scores = cross_val_score(clf, X, Y, cv =5)
    print (scores)

    # generates the clf and visualizes a decision tree
    #clf = clf.fit(X, Y)
    #dot_data = tree.export_graphviz(clf, out_file=None,
    #                                feature_names = feat, class_names = FEATURES.tactic.values,
    #                                filled = True, rounded = True)
    #graph = gv.Source(dot_data)
    #graph.render("picture")
