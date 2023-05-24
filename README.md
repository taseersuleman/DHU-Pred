# DHU prediction web app Information

**#Data/Files Information**

The deployed web app is live at https://dhu-prediction-app.herokuapp.com/

This web app predicts the Dihydrouridine Sites of RNA sequence

The web app was built in Python using the following libraries:
* streamlit
* biopython
* pandas
* numpy
* scikit-learn
* pickle

Following Files have been uploaded on the Github:

1) DHU-Prediction-app.py --> This file is the actual code file (In python), which is used to extract features of the RNA sequence data and then predict the sites as D-sites (Positive sites) or Non-D sites (Negative Sites)
2) Dhupred-RF.pkl = This is the pickle file of the trained model through which we get the optimized scores in all metrics while training.
3) Nucleotide_TRNA.png = This is the image which is displayed on the server.
4) Procfile = This is the mandatroy file for streamlit server to run.
5) requirements.txt = It contains all the relevant libraries required to run the DHU-Pred server.
6) setup.sh = This is the mandatroy file for streamlit server to run.
7) Sup1.fasta = This is fasta file contains the positive sites (modified or D sites).
8) Sup2.fasta = This is fasta file contains negative sites (Non-modified or Non-D sites).

**Execution Information**

1. Input the RNA sequence of any length in the sidebar of the application in "Sequence Input" section. Then click the "-Submit-" button.
2. For sample/test sequence, click "Example" button.
