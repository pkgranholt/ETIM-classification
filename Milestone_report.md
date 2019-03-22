# Capstone Project - Milestone Report

### The client
The Norwegian Electrical Trade Organisation (EFO) works for the suppliers and wholesalers of electrotechnical equipment and solutions. This spans products from a single lightbulb to the biggest infrastructure projects. With 500 member and customer companies, our members' portfolios cover almost every type of electrotechnical product.

We have a product database that suppliers, wholesalers and installers use to communicate about products and their properties. We have about 300,000 products registered with us, most of which are active and currently accessible. As part of our mission to be the connector between the different roles in our industry, we have carefully selected the properties that products that are registered with us need to have. We check the products that are registered with us to make sure they have the necessary data.

### The task
There are many standards that electrotechnical products need to be classified by. One of the most important ones is the ETIM (European Technical Information Model) classification model. There are at the time of writing 4725 ETIM classes. It is up to the member companies who own the products to correctly identify which ETIM class each product belongs to. There are [tools to look up the different classes](https://prod.etim-international.com/class# "ETIM-international's Classification Management Tool), but as a manual process, it can be time-consuming. EFO would like to assist in this task, by creating a machine learning model which can suggest which ETIM class each product belongs in, based on easily accessible product features.

### The data set
The data for this project was selected as a SQL-query from the EFO product database. Because of the size of the database and the extent of the query, it was decided that this will not be a part of this project. The first draft of the query (before optimisation) was estimated to run for about 30 hours in order to give all the output. There were then several rounds of optimisation, and the final query ran for about eight minutes on a regular computer.

There are different states that a product can have in the database. It can be a draft, active, retired or a handful of other states. The output of the initial query included all active products from the database and all features. This is a data frame with 238 049 active products, each with 125 features.

From all these 125 features, two were chosen based on the domain knowledge from the experts at EFO to predict the correct ETIM-class. These two features were chosen because they are presumed to be both easily accessible for all products, and the expectation is that they will be sufficient to recommend an ETIM-class.

The selected features are:

1) The electrical number group (ENG), which is a rough grouping of the products. For instance, all products in ENG 10 are either cables or products related to cables. This is on a much, much more aggregated level than the ETIM-classes, which specifies in more detail what kind of a product this is. To compare the level of detail: ETIM class 000080 is "Surface mounted housing for flush mounted switching device". The ENG narrows the scope of potential ETIM classes down quite a bit, and there are several reasons why one expects this to be correctly selected, so the chance of getting an incorrectly selected ENG is tiny.

2) The technical description of the product, which is a text field that describes the product. If the product is a lightbulb, the technical description might include information regarding Watts, Lumen, Socket type and so on. There are few rules on what the technical description can include, so while there's an expectation that this will be a very useful feature, it will be interesting to see if this is correct.

### The initial findings
The initial overview shows there are 41 ENGs, 1 814 ETIM-classes and 109 429 technical descriptions. The frequencies for all three are heavily skewed with long tails. This means selecting good cut-off points will be crucial for the model optimisation. It also means we shouldn't expect to be able to predict the rarest ETIM-classes, even though there are many of them. On the other hand, the most popular ETIM-classes should be fairly straightforward to predict. Unfortunately, the most used technical descriptions are the same for many products, which may warrant the removal of most frequent ones.

There were some thousands of products with missing data, in addition to products with bad technical descriptions. These are simply removed, and we're left with over 200 000 products after all data wrangling and cleaning. The biggest group of products that was removed was products without an ETIM-class, which if the project is successful, will be a true test group to predict the ETIM-class.

### The remaining work
Going forward, the technical descriptions need to be transformed into a corpus. We'll see how much stemming and lemmatization is necessary or useful. There are a lot of technical terms in the texts, so default stemmers might not be as useful as in many other texts. The same goes for lemmatization; with bad lemmatization, one might lose some of the useful differentiators between similar products that need to be differentiated.

The distributions of ETIM-classes within each ENG must be saved, and the data set needs to be split into train and test set. Finally, a combination of logistic regression and Naïve Bayes can be used to predict the ETIM-class within each ENG based on the technical description.
