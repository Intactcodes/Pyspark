# Databricks notebook source
import os
import pandas as pd

excel_file_path = 'output/output_excel_file.xlsx'  
excel_df = pd.read_excel(excel_file_path)
print(excel_df)
