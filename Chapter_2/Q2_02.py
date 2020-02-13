def copy(src, dst, recursive=False):
    print(f"copy {src} from {dst} (recursive: {recursive})")


copy('A', 'B', True)
copy("""①"""=True, """②"""='B', """③"""='A')
copy('A', dst='B')
