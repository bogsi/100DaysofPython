import statistics as st


def describe(sample):
    return st.mean(sample), st.median(sample), st.mode(sample)
