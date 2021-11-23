# Import data from csv and create matrices for each different wind-location
# To be used with the 7Kierros stan-models


# Change the path to yours
raw_data <- read.csv(file="/home/jalovaj2/notebooks/BDA_project/data_csv_23112021.csv", header=TRUE)

wind_maar <- raw_data[,4]
wind_kok <- raw_data[,5]
wind_kemi <- raw_data[,6]

wind_maar_matrix <- split(wind_maar, ceiling(seq_along(wind_maar)/12))
wind_kok_matrix <- split(wind_kok, ceiling(seq_along(wind_kok)/12))
wind_kemi_matrix <- split(wind_kemi, ceiling(seq_along(wind_kemi)/12))

wind_maar_matrix <- do.call(rbind, wind_maar_matrix)
wind_kok_matrix <- do.call(rbind, wind_kok_matrix)
wind_kemi_matrix <- do.call(rbind, wind_kemi_matrix)