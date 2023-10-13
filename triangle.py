{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "67a80fcf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "def triangle(a,b,c):\n",
    "    val = False\n",
    "    if a+b>=c:\n",
    "        if a+c>=b:\n",
    "            if c+b>=a:\n",
    "                val =True\n",
    "    return val\n",
    "print(triangle(4,2,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf77d0e0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
