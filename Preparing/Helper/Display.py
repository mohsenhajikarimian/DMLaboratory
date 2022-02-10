import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
def displayCorrelationDiagram(Input_train, Target_train):
        for targetColumn in Target_train.columns:
                Train_data = Input_train.copy()
                Train_data[targetColumn] = Target_train[targetColumn]
                # mpl.use("Agg")
                correlation_matrix = Train_data.corr()
                round(correlation_matrix,2)
                sns.heatmap(correlation_matrix, annot = True)
                plt.colorbar()
                plt.imshow(correlation_matrix)
                