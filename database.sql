-- ==== --
-- INIT --
-- ==== --

CREATE DATABASE IF NOT EXISTS spatula;
USE spatula;
DROP TABLE IF EXISTS recipe;
DROP TABLE IF EXISTS subCategory;
DROP TABLE IF EXISTS category;

-- ============= --
-- CREATE TABLES --
-- ============= --

CREATE TABLE category (
    categoryID int PRIMARY KEY,
    categoryTitle TEXT NOT NULL,
    categoryDescription TEXT NOT NULL
);

CREATE TABLE subCategory (
	categoryID int,
    subCategoryID int PRIMARY KEY,
    subCategoryName VARCHAR(100) NOT NULL,
    subCategoryTitle VARCHAR(255) NOT NULL,
    subCategoryDescription TEXT,
	FOREIGN KEY (categoryID) REFERENCES category(categoryID)
);

CREATE TABLE recipe (
    recipeID int AUTO_INCREMENT PRIMARY KEY,
    categoryID int,
    recipeTags VARCHAR(255) NOT NULL,
    recipeTitle VARCHAR(255) NOT NULL,
    recipeUploadData DATE NOT NULL,
    recipeImage VARCHAR(255) NOT NULL,
    recipeCookTime int NOT NULL,
    recipeAmount VARCHAR(255) NOT NULL,
    recipeIngredients TEXT NOT NULL,
    recipeInstructions TEXT NOT NULL,
	FOREIGN KEY (categoryID) REFERENCES category(categoryID)
);

-- =========== --
-- INSERT DATA --
-- =========== --

INSERT INTO category(categoryID, categoryTitle, categoryDescription)
VALUES
	(1, "Meal Type", "Browse by meal type."),
	(2, "Dish Type", "Browse by dish type."),
	(3, "Ingredient", "Browse by ingredient."),
	(4, "Cooking Style", "Browse by cooking style."),
	(5, "Diet and Health", "Browse by diet and health."),
	(6, "World Cuisine", "Browse by world cuisine");

INSERT INTO subCategory(categoryID, subCategoryID, subCategoryTitle, subCategoryDescription, subCategoryName)
VALUES
	-- Meal Type --
	(1, 1, "Appetizers and Snacks", "Perfect party appetizers made easy. See hundreds of tasty appetizers with photos and tips on how to make them.", "Appetizers and Snacks,,"),
	(1, 2, "Breakfast and Brunch", "Start your day with an easy pancake or omelet breakfast. Or with quiches, waffles, casseroles, and more!", "Breakfast and Brunch,,"),
	(1, 3, "Desserts", "We have most of the top-rated dessert recipes to satisfy your taste buds.", "Desserts,,"),
	(1, 4, "Dinner", "What's for dinner? Take the work out of searching for an answer to this question with these dinner recipes.", "Dinner,,"),
	(1, 5, "Drinks", "From cocktails to punch for kids, find the perfect party drink.", "Drinks,,"),
	-- Dish Type --
	(2, 6, "Breads", "See how to bake bread at home. Recipes for white, wheat, and more with photos, video, and tips to help you make them. Bread machine versions, too!", "Breads,,"),
	(2, 7, "Cakes", "See the best cake recipes. Trusted recipes for chocolate cake, white cake, banana cakes, and carrot cakes with photos and tips from home cooks.", "Cakes,,"),
	(2, 8, "Salads", "Find the best green salad recipes, plus trusted recipes for more than 3,550 other dinner and picnic salads.", "Salads,,"),
	(2, 9, "Smoothies", "Banana, strawberry, and dozens more fruit and vegetable smoothie recipes. Find a new healthy breakfast or snack today!", "Smoothies,,"),
	(2, 10, "Soups, Stews, and Chili", "Find recipes for hearty favorites like chicken tortilla soup, beef stew, white chicken chili, and more.", "Soup,,"),
	-- Ingredient --
	(3, 11, "Beef", "Beef stew, beef stroganoff, slow cooker pot roast: find the best beef recipes, including hundreds of ways to cook ground beef for tonight's dinner.", "Beef,,"),
	(3, 12, "Chicken", "Find recipes for fried chicken, chicken breast, grilled chicken, chicken wings, and more! spatula has more than 5,430 kitchen-approved chicken recipes.", "Chicken,,"),
	(3, 13, "Pasta", "Looking for main dish pasta recipes? spatula has more than 3000 trusted main dish pasta recipes.", "Pasta,,"),
	(3, 14, "Pork", "Pork tenderloin. Pork chops. Pulled pork. Hundreds of trusted recipes plus photos to help you cook pork right.", "Pork,,"),
	(3, 15, "Salmon", "Easy baked and grilled salmon recipes. See tasty seasoning and marinade ideas for salmon fillets, with tips from home cooks.", "Salmon,,"),
	-- Cooking Style --
	(4, 16, "BBQ and Grilling", "The best BBQ chicken, pork and BBQ sauces. Hundreds of barbecue and grilling recipes, with tips and tricks from home grillers.", "BBQ,,"),
	(4, 17, "Quick and Easy", "Explore thousands of top-rated, quick and easy recipes for breakfast, lunch, and dinner.", "Quick,,"),
	(4, 18, "Slow Cooker", "Find top-rated slow cooker recipes for chicken, pork, sandwich fillings, pot roasts, chili, stews, and more.", "Slow Cooker,,"),
	(4, 19, "Vegan", "Plant-based diets are healthier, environment-friendly, and really yummy. Our collection has over 1,940 real-people-tested vegan recipes for cooking and baking. Don't forget dessert!", "Vegan,,"),
	(4, 20, "Vegetarian", "Find easy vegetarian and vegan dinners for eating healthy. Hundreds of vegetarian recipes with photos.", "Vegetarian,,"),
	-- Diet and Health --
	(5, 21, "Diabetic", "Diabetic-friendly cakes, cookies, and more low-sugar desserts, plus dinner ideas. See more than 520 recipes for diabetics, tested and reviewed by home cooks.", "Diabetic,,"),
	(5, 22, "Gluten Free", "Delicious gluten-free cookies, desserts, and dinner recipes. Check out more than 1,430 gluten-free recipes, with helpful reviews from home cooks like you.", "Gluten,,"),
	(5, 23, "Healthy", "Find trusted recipes for eating healthy: start the day with a wholesome breakfast, cut the carbs or calories, find the perfect main dish for your special diet.", "Healthy,,"),
	(5, 24, "Low Calorie", "Find healthy, delicious low-calorie recipes including low-calorie breakfast, lunch, dinner and snacks from the food and nutrition experts at EatingWell.", "Low Calorie,,"),
	(5, 25, "Low Fat", "Low-fat chicken, chili, and sides. See hundreds of top low-fat recipes, including videos to help you make them. Find healthier dinners now!", "Low Fat,,"),
	-- World Cuisine --
	(6, 26, "Asian", "Super flavor, simple cooking. Get ideas for cooking Chinese, Japanese, Korean, Indian—the best of Asian cooking.", "Asian,,"),
	(6, 27, "Indian", "Explore the best of Indian cooking with these top-rated recipes for curries, tandoori chicken, chutneys, and more flavorful faves.", "Indian,,"),
	(6, 28, "Italian", "The best Italian-style pasta, chicken dishes, soup, and more. Traditional recipes with photos and videos to make them just like in the old country.", "Italian,,"),
	(6, 29, "Mexican", "Whether it's Taco Tuesday, Cinco de Mayo, or a Friday night, these recipes are fun enough for a party, and easy enough to make a delish weeknight dinner. Once you've tried all of these, we've got 50 amazing tacos for you to work your way through.", "Mexican,,"),
	(6, 30, "Southern", "Fried chicken and slaw. Grits and greens. Pulled pork and BBQ. These top-rated recipes show the best of the South.", "Southern,,");