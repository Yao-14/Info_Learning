"""
1.读取其他格式的数据转换为Dask Array
    from_array(x[, chunks, name, lock, asarray, ...]): Create dask array from something that looks like an array.
    from_delayed(value, shape[, dtype, meta, name]): Create a dask array from a dask delayed value
    from_npy_stack(dirname[, mmap_mode]): Load dask array from stack of npy files
    from_zarr(url[, component, storage_options, ...]): Load array from the zarr storage format
2.
    stack(seq[, axis, allow_unknown_chunksizes]): Stack arrays along a new axis
    concatenate(seq[, axis, ...]): Concatenate arrays along an existing axis
"""