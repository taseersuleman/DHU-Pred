import numpy as np
import pandas as pd
import streamlit as st
from Bio import SeqIO
import math
import csv
import pickle
from PIL import Image
from sklearn.preprocessing import StandardScaler

st.title(
    """
               DHU-Pred - Predictor for Dihydrouridine Sites in tRNA Sequences
"""
)
st.subheader("""The DHU-Pred is a web-server for the prediction of Dihydrouridine in transfer RNA (tRNA) modifications.
Dihydrouridine is formed from the uridine base by reducing the carbon-carbon double bond at positions 5 and 6 as shown in the Figure below. 
The current research study focused on the detection of D modification using a novel method for feature extraction from the RNA samples obtained from RMBase
containing 1035 Positive Samples from three species including Homosapiens (525) , Mus musculus (435), and Saccharomyces Cerevisiae (75) and 1396 Negative Samples.
Statistical moments are incorporated for the extraction and representation of feature vectors based on the position as well as the composition of nucleotide bases.
""")

#---------------------------------#
image = Image.open('Nucleotide_TRNA.png')
st.image(image)

str22 = "GGUUUCCGUAGUGUAGUGGUUAUCACGUUCGCCUCACACGC"
st.subheader("Kindly click the EXAMPLE button for sample RNA sequence")
if st.button('Example'):
    st.write(str22)