{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "01710604",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "entrer un nombre 56\n",
      "racine carre de [(2*50*nbr)/30]\n",
      "le result brut est:  13.662601021279464\n",
      "le result convertit est: 14\n",
      "le result convertit un chiffre apres la virgule est: 13.7\n"
     ]
    }
   ],
   "source": [
    "from math import *\n",
    "nbr= int(input('entrer un nombre '))\n",
    "print(\"racine carre de [(2*50*nbr)/30]\")\n",
    "Q=sqrt((2*50*nbr)/30)\n",
    "print('le result brut est: ', Q)\n",
    "print(\"le result convertit est: \" +format(Q,'.0f'))\n",
    "print(\"le result convertit un chiffre apres la virgule est: \"+ format(Q,'.1f'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fb08e665",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
