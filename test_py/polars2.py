    # ===============
    # Polars attempt.
    # lazy_df = pl.scan_ndjson(file, batch_size=rec)
    # lazy_df = lazy_df.slice(pos, rec).collect()
    # slice_list = lazy_df.rows()
    # child_logger.info(f"{process_id} - reached {rec:,} records tracked - inserting data")
    # # psycopg3 method.
    # with cursor.copy(f"COPY {schema}.{table} (json_object) FROM STDIN") as copy:
    #     for each_record in slice_list:
    #         copy.write_row(each_record)
    # conn.commit()
    # conn.close()
    # return
    # # ===============
