USE [bot_shop]
GO
/****** Object:  Table [dbo].[Administrators]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Administrators](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Login] [nvarchar](max) NULL,
	[Password] [nvarchar](max) NULL,
 CONSTRAINT [PK_Administrators] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Buyers]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Buyers](
	[id] [bigint] NOT NULL,
	[Name] [nvarchar](max) NULL,
	[Phone] [nvarchar](max) NULL,
 CONSTRAINT [PK_Buyers] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Cart]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Cart](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Good_id] [nchar](10) NULL,
	[Buyer_id] [bigint] NULL,
 CONSTRAINT [PK_Basket1] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Categories]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Categories](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Name_category] [nvarchar](max) NULL,
 CONSTRAINT [PK_Categories] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Goods]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Goods](
	[id] [nchar](10) NOT NULL,
	[Name] [nvarchar](max) NULL,
	[Price] [int] NULL,
	[Category_id] [int] NULL,
	[Material_id] [int] NULL,
	[Species_id] [int] NULL,
	[Photo_url] [nvarchar](max) NULL,
	[Size_range] [nchar](10) NULL,
 CONSTRAINT [PK_Goodss] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Materials]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Materials](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Name_material] [nvarchar](max) NULL,
 CONSTRAINT [PK_Materials] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Orders]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Orders](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Buyer_id] [bigint] NULL,
	[State] [nvarchar](max) NULL,
	[City] [nvarchar](max) NULL,
	[Street] [nvarchar](max) NULL,
 CONSTRAINT [PK_Orders] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Species]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Species](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[Name_species] [nvarchar](max) NULL,
 CONSTRAINT [PK_Species] PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[Cart]  WITH CHECK ADD  CONSTRAINT [FK_Cart_Buyers] FOREIGN KEY([Buyer_id])
REFERENCES [dbo].[Buyers] ([id])
GO
ALTER TABLE [dbo].[Cart] CHECK CONSTRAINT [FK_Cart_Buyers]
GO
ALTER TABLE [dbo].[Cart]  WITH CHECK ADD  CONSTRAINT [FK_Cart_Goods] FOREIGN KEY([Good_id])
REFERENCES [dbo].[Goods] ([id])
GO
ALTER TABLE [dbo].[Cart] CHECK CONSTRAINT [FK_Cart_Goods]
GO
ALTER TABLE [dbo].[Goods]  WITH CHECK ADD  CONSTRAINT [FK_Goods_Categories] FOREIGN KEY([Category_id])
REFERENCES [dbo].[Categories] ([id])
GO
ALTER TABLE [dbo].[Goods] CHECK CONSTRAINT [FK_Goods_Categories]
GO
ALTER TABLE [dbo].[Goods]  WITH CHECK ADD  CONSTRAINT [FK_Goods_Materials] FOREIGN KEY([Material_id])
REFERENCES [dbo].[Materials] ([id])
GO
ALTER TABLE [dbo].[Goods] CHECK CONSTRAINT [FK_Goods_Materials]
GO
ALTER TABLE [dbo].[Goods]  WITH CHECK ADD  CONSTRAINT [FK_Goods_Species] FOREIGN KEY([Species_id])
REFERENCES [dbo].[Species] ([id])
GO
ALTER TABLE [dbo].[Goods] CHECK CONSTRAINT [FK_Goods_Species]
GO
ALTER TABLE [dbo].[Orders]  WITH CHECK ADD  CONSTRAINT [FK_Orders_Buyers] FOREIGN KEY([Buyer_id])
REFERENCES [dbo].[Buyers] ([id])
GO
ALTER TABLE [dbo].[Orders] CHECK CONSTRAINT [FK_Orders_Buyers]
GO
/****** Object:  StoredProcedure [dbo].[AddBuyers]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE             procedure [dbo].[AddBuyers]
@id bigint, @Name nvarchar(MAX), @Phone nvarchar(MAX)
as
INSERT INTO Buyers(id, Name, Phone) VALUES (@id, @Name, @Phone)



GO
/****** Object:  StoredProcedure [dbo].[AddCart]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE                 procedure [dbo].[AddCart]
@Good_id nvarchar(10), @Buyer_id bigint
as
begin
insert into Cart(Good_id, Buyer_id) values (@Good_id, @Buyer_id)
end
GO
/****** Object:  StoredProcedure [dbo].[AddCategories]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Create           procedure [dbo].[AddCategories]
@NameCategory nvarchar(max)
as
insert into Categories(Name_category) values(@NameCategory)
GO
/****** Object:  StoredProcedure [dbo].[AddGoods]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE             procedure [dbo].[AddGoods]
@id nvarchar(10), @Name nvarchar(MAX), @Price int, @Category_name nvarchar(MAX), @Material_name nvarchar(MAX),
@Species_name nvarchar(MAX), @Photo_url nvarchar(MAX), @Size_range nvarchar(10)
as
begin
DECLARE @Category_id int, @Material_id int, @Species_id int
set @Material_id = (select id from Materials where Name_material = @Material_name);
set @Category_id = (select id from Categories where Name_category = @Category_name); 
set @Species_id = (select id from Species where Name_species = @Species_name);

if (@Material_id IS NOT NULL and @Category_id IS NOT NULL and @Species_id IS NOT NULL)
	begin
	insert into Goods(id, Name, Price, Category_id, Material_id, Species_id, Photo_url, Size_range)
	values(@id, @Name, @Price, @Category_id, @Material_id, @Species_id, @Photo_url, @Size_range)
	end
end
GO
/****** Object:  StoredProcedure [dbo].[AddMaterials]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE         procedure [dbo].[AddMaterials]
@NameMaterial nvarchar(max)
as
insert into Materials(Name_material) values(@NameMaterial)
GO
/****** Object:  StoredProcedure [dbo].[AddOrders]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE                   procedure [dbo].[AddOrders]
@Buyer_id bigint, @State nvarchar(MAX), @City nvarchar(MAX), @Street nvarchar(MAX)
as
begin
insert into Orders(Buyer_id, State, City, Street) values (@Buyer_id, @State, @City, @Street)
end
GO
/****** Object:  StoredProcedure [dbo].[AddSpecies]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Create           procedure [dbo].[AddSpecies]
@NameSpecies nvarchar(max)
as
insert into Species(Name_species) values(@NameSpecies)
GO
/****** Object:  StoredProcedure [dbo].[DellAllCategories]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Create             procedure [dbo].[DellAllCategories]
as
DELETE FROM Categories
GO
/****** Object:  StoredProcedure [dbo].[DellAllGoods]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create               procedure [dbo].[DellAllGoods]
as
DELETE FROM Goods
GO
/****** Object:  StoredProcedure [dbo].[DellAllMaterials]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Create             procedure [dbo].[DellAllMaterials]
as
DELETE FROM Materials
GO
/****** Object:  StoredProcedure [dbo].[DellAllSpecies]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
Create             procedure [dbo].[DellAllSpecies]
as
DELETE FROM Species
GO
/****** Object:  StoredProcedure [dbo].[DellCart]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create               procedure [dbo].[DellCart]
as
DELETE FROM Cart
GO
/****** Object:  StoredProcedure [dbo].[DellGoodInCartById]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE                 procedure [dbo].[DellGoodInCartById]
@Good_id nvarchar(10), @Buyer_id bigint
as
DELETE FROM Cart WHERE Cart.Good_id = @Good_id and Cart.Buyer_id = @Buyer_id
GO
/****** Object:  StoredProcedure [dbo].[ShowAdministrators]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create             procedure [dbo].[ShowAdministrators]
@Login nvarchar(MAX), @Password nvarchar(MAX)
as
SELECT COUNT(*) FROM Administrators WHERE Administrators.Login = @Login and Administrators.Password = @Password
GO
/****** Object:  StoredProcedure [dbo].[ShowBuyers]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE             procedure [dbo].[ShowBuyers]
@id bigint
as
SELECT COUNT(*) FROM Buyers WHERE Buyers.id = @id



GO
/****** Object:  StoredProcedure [dbo].[ShowCart]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE                 procedure [dbo].[ShowCart]
@Buyer_id bigint
as
begin
SELECT Cart.Good_id AS GoodsId,
	Goods.Name AS GoodsName,
	Goods.Price AS Price,
	Goods.Photo_url AS Photo,
	COUNT(*) AS Count
FROM Cart
INNER JOIN Goods ON Cart.Good_id = Goods.id
WHERE Cart.Buyer_id = @Buyer_id
GROUP BY Cart.Good_id, Goods.Name, Goods.Price, Goods.Photo_url
HAVING COUNT(*) >= 1;
end
GO
/****** Object:  StoredProcedure [dbo].[ShowGoods]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create               procedure [dbo].[ShowGoods]
@Name_category nvarchar(Max), @Name_species nvarchar(Max)
as
begin
DECLARE @Category_id int, @Species_id int
set @Category_id = (select id from Categories where Categories.Name_category = @Name_category);
set @Species_id = (select id from Species where Species.Name_species = @Name_species);

select Goods.id, Goods.Name, Goods.Price, Categories.Name_category, Materials.Name_material, Species.Name_species, Goods.Photo_url, Goods.Size_range 
from Goods

join Categories on Categories.id = Goods.Category_id
join Materials on Materials.id = Goods.Material_id
join Species on Species.id = Goods.Species_id

where Goods.Species_id = @Species_id and Categories.id = @Category_id
end
GO
/****** Object:  StoredProcedure [dbo].[ShowGoodsId]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create                 procedure [dbo].[ShowGoodsId]
as
begin
select Goods.id from Goods
end
GO
/****** Object:  StoredProcedure [dbo].[UploadCategories]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create                 procedure [dbo].[UploadCategories]
as
begin
select Categories.id, Categories.Name_category
from Categories
end
GO
/****** Object:  StoredProcedure [dbo].[UploadGoods]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create                 procedure [dbo].[UploadGoods]
as
begin

select Goods.id, Goods.Name, Goods.Price, Goods.Category_id, Goods.Material_id, Goods.Species_id, Goods.Photo_url, Goods.Size_range 
from Goods
end
GO
/****** Object:  StoredProcedure [dbo].[UploadMaterials]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create                 procedure [dbo].[UploadMaterials]
as
begin
select Materials.id, Materials.Name_material
from Materials
end
GO
/****** Object:  StoredProcedure [dbo].[UploadOrders]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create                 procedure [dbo].[UploadOrders]
as
begin
select Orders.id, Orders.Buyer_id, Orders.State, Orders.City, Orders.Street
from Orders
end
GO
/****** Object:  StoredProcedure [dbo].[UploadSpecies]    Script Date: 26.06.2023 16:43:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
create                 procedure [dbo].[UploadSpecies]
as
begin
select Species.id, Species.Name_species
from Species
end
GO
