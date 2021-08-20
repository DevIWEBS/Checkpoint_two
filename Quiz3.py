{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6f1fb542",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrer un nombre svp 5\n",
      "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}\n"
     ]
    }
   ],
   "source": [
    "nbr=int(input('Entrer un nombre svp '))\n",
    "\n",
    "data= dict()\n",
    "for i in range(1,nbr+1):\n",
    "    data[i]=i*i\n",
    "print(data)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "26193033",
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
