from crewai_tools import DirectoryReadTool

#add all the related financial documents about the company which you want in to see the results
statements_reader_tool = DirectoryReadTool(directory=r"D:\crewAI-examples-main\stock_analysis\src\stock_analysis\tools\results_company")
