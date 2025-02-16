# pydantic在fish中会自动从fish shell中提取变量，而不是指定的.env

如果fish中没有设定，则会提取.env，即便使用了load_dotenv()也没有用
