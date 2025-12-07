{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b7e58c0f-fc04-4d97-bbf8-2943526d256d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['andaman-&-nicobar-islands',\n",
       " 'andhra-pradesh',\n",
       " 'arunachal-pradesh',\n",
       " 'assam',\n",
       " 'bihar',\n",
       " 'chandigarh',\n",
       " 'chhattisgarh',\n",
       " 'dadra-&-nagar-haveli-&-daman-&-diu',\n",
       " 'delhi',\n",
       " 'goa',\n",
       " 'gujarat',\n",
       " 'haryana',\n",
       " 'himachal-pradesh',\n",
       " 'jammu-&-kashmir',\n",
       " 'jharkhand',\n",
       " 'karnataka',\n",
       " 'kerala',\n",
       " 'ladakh',\n",
       " 'lakshadweep',\n",
       " 'madhya-pradesh',\n",
       " 'maharashtra',\n",
       " 'manipur',\n",
       " 'meghalaya',\n",
       " 'mizoram',\n",
       " 'nagaland',\n",
       " 'odisha',\n",
       " 'puducherry',\n",
       " 'punjab',\n",
       " 'rajasthan',\n",
       " 'sikkim',\n",
       " 'tamil-nadu',\n",
       " 'telangana',\n",
       " 'tripura',\n",
       " 'uttar-pradesh',\n",
       " 'uttarakhand',\n",
       " 'west-bengal']"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import pyodbc\n",
    "import json\n",
    "import os\n",
    "\n",
    "conn = pyodbc.connect(\n",
    "    'DRIVER={SQL Server};'\n",
    "    'SERVER=SAM\\SQLEXPRESS;'\n",
    "    'DATABASE=PhonePe1;'\n",
    "    'Trusted_Connection=yes;'\n",
    ")\n",
    "cursor = conn.cursor()\n",
    "import os\n",
    "\n",
    "path1 = \"C:/Users/Admin/Downloads/pulse-master/pulse-master/data/aggregated/transaction/country/india/state/\"\n",
    "os.listdir(path1)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "2d4168e0-cfa8-4fd3-bf50-e373c2c5a1a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import pyodbc\n",
    "import sqlalchemy\n",
    "\n",
    "\n",
    "\n",
    "conn = pyodbc.connect(\n",
    "    \"Driver={SQL Server};\"\n",
    "    \"Server=SAM\\SQLEXPRESS;\"  \n",
    "    \"Database=phonepe1;\"\n",
    "    \"Trusted_Connection=yes;\"\n",
    ")\n",
    "\n",
    "cursor = conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "c26cf9ae-d16d-4618-92c3-fdae45708a51",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data = {'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']}\n",
    "df = pd.DataFrame(data)\n",
    "data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "d8e2fcbc-d588-45d3-9f80-c28276cb843b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pyodbc in c:\\users\\admin\\anaconda3\\lib\\site-packages (5.2.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pyodbc\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "4ed63adb-f263-48a0-a3a6-7a1461c1d095",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\admin\\anaconda3\\lib\\site-packages (2.2.3)\n",
      "Requirement already satisfied: numpy in c:\\users\\admin\\anaconda3\\lib\\site-packages (2.1.3)\n",
      "Requirement already satisfied: matplotlib in c:\\users\\admin\\anaconda3\\lib\\site-packages (3.10.0)\n",
      "Requirement already satisfied: seaborn in c:\\users\\admin\\anaconda3\\lib\\site-packages (0.13.2)\n",
      "Requirement already satisfied: pyodbc in c:\\users\\admin\\anaconda3\\lib\\site-packages (5.2.0)\n",
      "Requirement already satisfied: sqlalchemy in c:\\users\\admin\\anaconda3\\lib\\site-packages (2.0.39)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from pandas) (2025.2)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from matplotlib) (1.3.1)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from matplotlib) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from matplotlib) (4.55.3)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from matplotlib) (1.4.8)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from matplotlib) (24.2)\n",
      "Requirement already satisfied: pillow>=8 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from matplotlib) (11.1.0)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from matplotlib) (3.2.0)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from sqlalchemy) (3.1.1)\n",
      "Requirement already satisfied: typing-extensions>=4.6.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from sqlalchemy) (4.12.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n"
     ]
    }
   ],
   "source": [
    "!pip install pandas numpy matplotlib seaborn pyodbc sqlalchemy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "774f78ea-68f8-4765-a441-0e3ca9450fca",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'aggregated_transaction_2021.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[37], line 12\u001b[0m\n\u001b[0;32m      4\u001b[0m conn \u001b[38;5;241m=\u001b[39m pyodbc\u001b[38;5;241m.\u001b[39mconnect(\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mDRIVER=\u001b[39m\u001b[38;5;124m{\u001b[39m\u001b[38;5;124mSQL Server};\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m      6\u001b[0m     \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mSERVER=SAM\u001b[39m\u001b[38;5;124m\\\u001b[39m\u001b[38;5;124mSQLEXPRESS;\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m      7\u001b[0m     \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mDATABASE=PhonePe1;\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m      8\u001b[0m     \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mTrusted_Connection=yes;\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m      9\u001b[0m )\n\u001b[0;32m     10\u001b[0m cursor \u001b[38;5;241m=\u001b[39m conn\u001b[38;5;241m.\u001b[39mcursor()\n\u001b[1;32m---> 12\u001b[0m df \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124maggregated_transaction_2021.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     14\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m index,row \u001b[38;5;129;01min\u001b[39;00m df\u001b[38;5;241m.\u001b[39miterrows():\n\u001b[0;32m     15\u001b[0m     cursor\u001b[38;5;241m.\u001b[39mexecute(\u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[0;32m     16\u001b[0m \u001b[38;5;124m        INSERT INTO aggregated_transaction \u001b[39m\n\u001b[0;32m     17\u001b[0m \u001b[38;5;124m        (year, quarter, state, district, pincode, payment_category, txn_count, txn_amount, unique_users)\u001b[39m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     20\u001b[0m     row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124myear\u001b[39m\u001b[38;5;124m'\u001b[39m], row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mquarter\u001b[39m\u001b[38;5;124m'\u001b[39m], row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstate\u001b[39m\u001b[38;5;124m'\u001b[39m], row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mdistrict\u001b[39m\u001b[38;5;124m'\u001b[39m], row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mpincode\u001b[39m\u001b[38;5;124m'\u001b[39m],\n\u001b[0;32m     21\u001b[0m     row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mpayment_category\u001b[39m\u001b[38;5;124m'\u001b[39m], row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtxn_count\u001b[39m\u001b[38;5;124m'\u001b[39m], row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtxn_amount\u001b[39m\u001b[38;5;124m'\u001b[39m], row[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124munique_users\u001b[39m\u001b[38;5;124m'\u001b[39m])\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1026\u001b[0m, in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, date_format, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options, dtype_backend)\u001b[0m\n\u001b[0;32m   1013\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[0;32m   1014\u001b[0m     dialect,\n\u001b[0;32m   1015\u001b[0m     delimiter,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1022\u001b[0m     dtype_backend\u001b[38;5;241m=\u001b[39mdtype_backend,\n\u001b[0;32m   1023\u001b[0m )\n\u001b[0;32m   1024\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[1;32m-> 1026\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m _read(filepath_or_buffer, kwds)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:620\u001b[0m, in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    617\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    619\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[1;32m--> 620\u001b[0m parser \u001b[38;5;241m=\u001b[39m TextFileReader(filepath_or_buffer, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[0;32m    622\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[0;32m    623\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1620\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m   1617\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m   1619\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m-> 1620\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_make_engine(f, \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mengine)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\parsers\\readers.py:1880\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[1;34m(self, f, engine)\u001b[0m\n\u001b[0;32m   1878\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m mode:\n\u001b[0;32m   1879\u001b[0m         mode \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1880\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;241m=\u001b[39m get_handle(\n\u001b[0;32m   1881\u001b[0m     f,\n\u001b[0;32m   1882\u001b[0m     mode,\n\u001b[0;32m   1883\u001b[0m     encoding\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1884\u001b[0m     compression\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcompression\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1885\u001b[0m     memory_map\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmemory_map\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mFalse\u001b[39;00m),\n\u001b[0;32m   1886\u001b[0m     is_text\u001b[38;5;241m=\u001b[39mis_text,\n\u001b[0;32m   1887\u001b[0m     errors\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mencoding_errors\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstrict\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1888\u001b[0m     storage_options\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mstorage_options\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m),\n\u001b[0;32m   1889\u001b[0m )\n\u001b[0;32m   1890\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1891\u001b[0m f \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles\u001b[38;5;241m.\u001b[39mhandle\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pandas\\io\\common.py:873\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    868\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    869\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[0;32m    870\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[0;32m    871\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[0;32m    872\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[1;32m--> 873\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(\n\u001b[0;32m    874\u001b[0m             handle,\n\u001b[0;32m    875\u001b[0m             ioargs\u001b[38;5;241m.\u001b[39mmode,\n\u001b[0;32m    876\u001b[0m             encoding\u001b[38;5;241m=\u001b[39mioargs\u001b[38;5;241m.\u001b[39mencoding,\n\u001b[0;32m    877\u001b[0m             errors\u001b[38;5;241m=\u001b[39merrors,\n\u001b[0;32m    878\u001b[0m             newline\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    879\u001b[0m         )\n\u001b[0;32m    880\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    881\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[0;32m    882\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'aggregated_transaction_2021.csv'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import pyodbc\n",
    "\n",
    "conn = pyodbc.connect(\n",
    "    'DRIVER={SQL Server};'\n",
    "    'SERVER=SAM\\SQLEXPRESS;'\n",
    "    'DATABASE=PhonePe1;'\n",
    "    'Trusted_Connection=yes;'\n",
    ")\n",
    "cursor = conn.cursor()\n",
    "\n",
    "df = pd.read_csv(\"aggregated_transaction_2021.csv\")\n",
    "\n",
    "for index,row in df.iterrows():\n",
    "    cursor.execute(\"\"\"\n",
    "        INSERT INTO aggregated_transaction \n",
    "        (year, quarter, state, district, pincode, payment_category, txn_count, txn_amount, unique_users)\n",
    "        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)\n",
    "    \"\"\", \n",
    "    row['year'], row['quarter'], row['state'], row['district'], row['pincode'],\n",
    "    row['payment_category'], row['txn_count'], row['txn_amount'], row['unique_users'])\n",
    "\n",
    "conn.commit()\n",
    "print(\"Data inserted successfully\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c163fa45-16ac-4546-a5e8-7dd206946fa8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
