# DBT

Since the past few portions have been covering the extracting and loading part of ELT, now the time has come for the Transformation portion of the project. Data build tool [DBT](https://www.getdbt.com/) is an efficient transformation tool that offers both cloud and CLI options to transform their data more effectively. It rests ontop of the data warehouse and can be productionalized to create different views for different roles/purposes through their ```models```.

We will be requiring transformations on certain fields as well as any extra metrics I thought were useful. My DBT project can be found [here](https://github.com/jaytar0/DE_anime_dbt) in the ```/models/analytics_dev``` directory.


## Steps
First and foremost we need to setup DBT, there should be a 14-day free trial for the cloud version where you get an IDE versus the open source free CLI that I would have normally been using. I thought it would be good practice here since this is most likely what orgs and companies use.

1. Create your dbt account.
2. Setup your database connection via their wizard, DBT does a good job as they pretty much just spoon feed you during this process.
3. If you have a github account there are ways to link a repository you can find more in their getting setup section [here](https://docs.getdbt.com/docs/get-started/getting-started/set-up-dbt-cloud)
4. After you are linked up to your db there should be an initialize project button.
5. Congrats! You are now in the IDE connected with the snowflake/postgresql warehouse.


![image](/assets/dbt_cloud_ui.png)


Now we can begin our work with ```models``` which include files like ```<model>.sql``` and ```schema.yml```. Both of these will determine in DBTs own way of how your transformations will be defined. Of course, there are many things you can do here and to be honest this tool is relatively new to me having done transformations with pandas/polars before, so if you want more details you will have to reference the [docs](https://docs.getdbt.com/docs/get-started/getting-started/set-up-dbt-cloud).

Here is an example of one of my models.


![image](/assets/dbt_environment.png)


They even provide useful integrations like logs and model lineage, even though I don't have much of one right now.


![image](/assets/dbt_lineage.png)


After I had everything sorted out with my models and defining my schemas I ran...

``` 
dbt run
dbt test
``` 

Commit the changes to github and then verify via ```snowflake worksheet``` to see if changes were reflected.


![image](/assets/snowflake_dbt_results.png)


Awesome, Transformation process complete!

> I am far from calling myself an expert on DBT processes, but so far I can see much value in it being the most popular way to transform data. I love it!


[Back](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/dbt_process.md) | [Next Step](https://github.com/jaytar0/DE_flow_anime_2022/blob/main/md_collection/dash.md)
