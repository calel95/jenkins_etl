import duckdb 
import pandas as pd

class Transform:
    def __init__(self,df) -> None:
        #self.file_path = file_path
        self.df = df


    def select_table(self):
        """Exibe o DataFrame atual."""
        print(self.df)
    
    def filter_select(self,query,save_df = False):
        """Filtra o DataFrame com uma consulta SQL, considerar o nome da tabela como VW.       
        Args:
            query (str): A consulta SQL.
            save_df (bool): Se True, salva o resultado no DataFrame original.       
        Returns:
            Retorna o dataframe original antes da edicao ou depois da edicao dependendo do parametro save_df.
        """
        duckdb.register('VW', self.df)
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            print(duckdb.df(result))
            return self.df
        
    def remove_data_duplicates(self):
        """Remove todos os registros duplicados."""
        duckdb.register('VW', self.df)
        count = duckdb.query("select count(*) from VW").df()
        query = "select distinct * from VW"
        result = duckdb.query(query).df()
        self.df = duckdb.df(result)
        duckdb.register('VW', self.df)
        count_after = duckdb.query("select count(*) from VW").df()
        print(f"linhas removidas: {count - count_after}")
        return self.df
    
    def remove_data_nulls(self,columns: list):
        """Remove todos os registros nulos de uma ou varias colunas.       
        Args:
            save_df (bool): Se True, salva o resultado no DataFrame original. 
            columns (list): Rece uma lista das colunas que devem ser verificadas se existe registros null      
        Returns:
            Retorna o dataframe original antes da edicao ou depois da edicao dependendo do parametro save_df.
        """
        duckdb.register('VW', self.df)
        if not isinstance(columns, list):
            columns = [columns]
        
        where_clause = " AND ".join([f"{column} IS NOT NULL" for column in columns])
        where_clause_drop_registers = " OR ".join([f"{column} IS NULL" for column in columns])
        
        query = f"SELECT * FROM VW WHERE {where_clause}"
        query_drop_registers = f"SELECT * FROM VW WHERE {where_clause_drop_registers}"

        print("=========================REGISTROS DROPADOS COM REGISTROS NULLS NOS CAMPOS ESPECIFICADOS=========================")
        result2 = duckdb.query(query_drop_registers).df()
        result = duckdb.query(query).df()
        print(duckdb.df(result2))
        self.df = duckdb.df(result)
        return self.df
    
    def last_position_data(self,column_order_by,column_partition_by,save_df = False, column_filter = '1=1'):
        duckdb.register('VW', self.df)
        query = f"SELECT * EXCLUDE(rn) from (select *, ROW_NUMBER() OVER(PARTITION BY {column_partition_by} order by {column_order_by} desc)as rn from VW) where rn = 1 AND {column_filter}"
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            print(duckdb.df(result))
            return self.df
    
    def first_position_data(self,column_order_by,column_partition_by,save_df = False,column_filter = '1=1'):
        duckdb.register('VW', self.df)
        query = f"SELECT * EXCLUDE(rn) from (select *, ROW_NUMBER() OVER(PARTITION BY {column_partition_by} order by {column_order_by} asc)as rn from VW) where rn = 1 AND {column_filter}"
        result = duckdb.query(query).df()
        if save_df:
            self.df = duckdb.df(result)
            return self.df
        else:
            print(duckdb.df(result))
            return self.df
        
    def apply_transformations(self, options):
        if 'remove_duplicates' in options:
            self.df = self.remove_data_duplicates(self.df)
        if 'remove_nulls' in options:
            self.df = self.remove_data_nulls(self.df, options['null_columns'])
        if 'last_position' in options:
            self.df = self.last_position_data(self.df, options['order_by'], options['partition_by'])
        # Adicione mais transformações conforme necessário
        return self.df