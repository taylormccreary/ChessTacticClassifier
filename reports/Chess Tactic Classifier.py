
# coding: utf-8

# # Chess Tactic Classifier

# ## Introduction

# _In chess, a tactic refers to a sequence of moves that limits the opponent's options and may result in tangible gain. (Wikipedia)_
# 
# Chess players often solve many tactics of a single theme in order to improve their pattern recognition skills. In order to enable this, chess websites such as Chess.com need to assign labels to the tactics in their large databases of tactics. Often this is done manually, by users tagging tactics with the themes they believe are relevant.
# 
# Our goal with this project is to automate that process of tagging for a small subset of tactic themes.

# ## Web Scraping

# First, we need to gather the data by scraping tactic information from Chess.com. To do this we'll use the package BeautifulSoup:

# In[7]:


from bs4 import BeautifulSoup


# Next, we'll load a module we wrote to take care of some of the web scraping details:

# In[18]:


#load ..\..\src\url_utils


# In[14]:


lsmagic

