a
    nR�a  �                   @   s�   d dl Zd dlZd dlmZ g d�Zg d�Zdd� Zeee�Z	e
e	� dd� Zd	Zd
Zeee�Ze
e� dd� ZdZdd� Ze
e� � dd� Ze
ee�� dd� Zee�d	dejgejejdgd���Ze
e� dS )�    N)�train_test_split)�blueZlargeZgrainyZsubstantialZpotentZthermonuclear)ZfoodZhouseZtreeZbicycleZtoupeeZphonec                 C   s   t j�| �d t j�|� S )z*random combination of adjectives and nouns� )�np�random�choice)�
Adjectives�Nouns� r
   �JC:\Users\rozan\onedrive\desktop\lambdata-ds33\lambdata\helper_functions.py�random_phrase   s    r   c                 C   s   t �| |d�}t j�|�S )Ng�������?)r   Zaranger   r   )�min_val�max_valZrfr
   r
   r   �random_float   s    r   �   �   c                 C   s   t j�| �}|S �N)r   r   �randint)�intZrintr
   r
   r   �random_bowling_score   s    r   i,  c                   C   s   t tt�ttt�tt�fS r   )r   r   r	   r   r   r   r   r   r
   r
   r
   r   �silly_tuple   s    r   c                 C   s   t j�t� | �S r   )r   r   r   r   )Z
num_tuplesr
   r
   r   �silly_tuple_list"   s    r   c                 C   s   | � � �� �� S )zBreturns the number of null values 
    across the entire dataframe)Zisnull�sum)�dfr
   r
   r   �
null_count'   s    r   �   �   )�x�y)ZpandasZpdZnumpyr   Zsklearn.model_selectionr   r   r	   r   Zrphrase�printr   r   r   Zrfloatr   r   r   r   r   Z	DataFrameZNaNr   r
   r
   r
   r   �<module>   s*   


&