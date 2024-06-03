import pandas as pd
import flet as ft
import googlemaps

# Initialize the client
gmaps = googlemaps.Client(key='AIzaSyB2URgchBS3nhUTufYBP0KL1nUoX3ylueM')
# AIzaSyB2URgchBS3nhUTufYBP0KL1nUoX3ylueM

nutrition_df = pd.read_excel('nutrition.xlsx')

food = nutrition_df['餐點']
ingredient = nutrition_df['食物原料']
meat_vegan_type = nutrition_df['葷素']
protein = nutrition_df['蛋白質(g)']
carbs = nutrition_df['碳水化合物(g)']
fat = nutrition_df['脂肪(g)']

# calories=4*(protein+carbs)+9*fat
ingredient = ingredient.str.split("、")
# print(len(food))
# for i in range(len(food)):
#    print(food[i])

# max_calories_index=calories.idxmax()
# print("The highest calories: ",food[max_calories_index])
# print("The calories: ",calories[max_calories_index])
# print(ingredient[max_calories_index])
# print(meat_vegan_type[max_calories_index])

# min_calories_index=calories.idxmin()
# print("The lowest calories: ",food[min_calories_index])
# print("The calories: ",calories[min_calories_index])
# print(ingredient[min_calories_index])
# print(meat_vegan_type[min_calories_index])

noodle = []
noodle_protein = []
noodle_carbs = []
noodle_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '麵條':
            noodle.append(food[i])
            noodle_protein.append(protein[i])
            noodle_carbs.append(carbs[i])
            noodle_fat.append(fat[i])
# print(len(noodle))
# print(len(noodle_protein))
# print(len(noodle_carbs))
# print(len(noodle_fat))

rice = []
rice_protein = []
rice_carbs = []
rice_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '米飯':
            rice.append(food[i])
            rice_protein.append(protein[i])
            rice_carbs.append(carbs[i])
            rice_fat.append(fat[i])
# print(len(rice))

vegetable = []
vegetable_protein = []
vegetable_carbs = []
vegetable_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '蔬菜':
            vegetable.append(food[i])
            vegetable_protein.append(protein[i])
            vegetable_carbs.append(carbs[i])
            vegetable_fat.append(fat[i])
# print(vegetable)

pork = []
pork_protein = []
pork_carbs = []
pork_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '豬肉':
            pork.append(food[i])
            pork_protein.append(protein[i])
            pork_carbs.append(carbs[i])
            pork_fat.append(fat[i])
# print(len(pork))

chicken = []
chicken_protein = []
chicken_carbs = []
chicken_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '雞肉':
            chicken.append(food[i])
            chicken_protein.append(protein[i])
            chicken_carbs.append(carbs[i])
            chicken_fat.append(fat[i])
# print(len(chicken))

beef = []
beef_protein = []
beef_carbs = []
beef_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '牛肉':
            beef.append(food[i])
            beef_protein.append(protein[i])
            beef_carbs.append(carbs[i])
            beef_fat.append(fat[i])
# print(beef_meat)

egg = []
egg_protein = []
egg_carbs = []
egg_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '雞蛋':
            egg.append(food[i])
            egg_protein.append(protein[i])
            egg_carbs.append(carbs[i])
            egg_fat.append(fat[i])
# print(egg)
tofu = []
tofu_protein = []
tofu_carbs = []
tofu_fat = []
for i in range(len(food)):
    for j in range(len(ingredient[i])):
        if ingredient[i][j] == '豆腐':
            tofu.append(food[i])
            tofu_protein.append(protein[i])
            tofu_carbs.append(carbs[i])
            tofu_fat.append(fat[i])
# print(tofu)


def calculate_daily_calories(gender, height, weight, age, activity_level):
    if gender == "male":
        bmr = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif gender == "female":
        bmr = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    else:
        print("Invalid gender input. Please choose '1' for male or '2' for female.")
        return

    activity_levels = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "high": 1.725,
        "very high": 1.9
    }

    if (activity_level == "sedentary"):
        total_calories = bmr * 1.2
        protein = weight * 0.8  # 蛋白質需求公式
        carbs = total_calories * 0.5 / 4  # 碳水化合物需求公式
        fat = total_calories * 0.3 / 9  # 脂肪需求公式
    elif (activity_level == "light"):
        total_calories = bmr * 1.2
        protein = weight * 0.8  # 蛋白質需求公式
        carbs = total_calories * 0.5 / 4  # 碳水化合物需求公式
        fat = total_calories * 0.3 / 9  # 脂肪需求公式
    elif (activity_level == "moderate"):
        total_calories = bmr * 1.2
        protein = weight * 0.8  # 蛋白質需求公式
        carbs = total_calories * 0.5 / 4  # 碳水化合物需求公式
        fat = total_calories * 0.3 / 9  # 脂肪需求公式
    elif (activity_level == "high"):
        total_calories = bmr * 1.2
        protein = weight * 0.8  # 蛋白質需求公式
        carbs = total_calories * 0.5 / 4  # 碳水化合物需求公式
        fat = total_calories * 0.3 / 9  # 脂肪需求公式
    elif (activity_level == "very high"):
        total_calories = bmr * 1.2
        protein = weight * 0.8  # 蛋白質需求公式
        carbs = total_calories * 0.5 / 4  # 碳水化合物需求公式
        fat = total_calories * 0.3 / 9  # 脂肪需求公式

    return total_calories, protein, carbs, fat
    # else:
    #     print("Invalid activity level input. Please choose from the following options:")
    #     for level in activity_levels:
    #         print("-", level)
    #     return


def meat_vegan_decide(meat_vegan_choice, food_list, ingredient_list, protein_list, carbs_list, fat_list, calories_list):
    # 選擇葷/素
    food = nutrition_df['餐點']
    ingredient = nutrition_df['食物原料']
    meat_vegan_type = nutrition_df['葷素']
    protein = nutrition_df['蛋白質(g)']
    carbs = nutrition_df['碳水化合物(g)']
    fat = nutrition_df['脂肪(g)']
    # calories=4*(protein+carbs)+9*fat

    if meat_vegan_choice == 1:
        for i in range(len(food)):
            if (meat_vegan_type[i] == "葷"):
                food_list.append(food[i])
                ingredient_list.append(ingredient[i])
                protein_list.append(protein[i])
                carbs_list.append(carbs[i])
                fat_list.append(fat[i])
    elif meat_vegan_choice == 2:
        for i in range(len(food)):
            if (meat_vegan_type[i] == "素"):
                food_list.append(food[i])
                ingredient_list.append(ingredient[i])
                protein_list.append(protein[i])
                carbs_list.append(carbs[i])
                fat_list.append(fat[i])
    elif meat_vegan_choice == 3:
        for i in range(len(food)):
            food_list.append(food[i])
            ingredient_list.append(ingredient[i])
            protein_list.append(protein[i])
            carbs_list.append(carbs[i])
            fat_list.append(fat[i])
    else:
        print("Invalid meat/vegan choice. Please try again.")
    for i in range(len(food_list)):
        calories_list.append(4*(protein_list[i]+carbs_list[i])+9*fat_list[i])


def food_classification_decide(selected_food, food_list, protein_list, carbs_list, fat_list):
    # 選擇葷素後，選擇偏好食物類別
    flag = 0

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "麵條"):
                food_intersection = list(set(food_list) & set(noodle))
                protein_intersection = list(
                    set(protein_list) & set(noodle_protein))
                carbs_intersection = list(set(carbs_list) & set(noodle_carbs))
                fat_intersection = list(set(fat_list) & set(noodle_fat))
                selected_food.remove("麵條")
                # print(selected_food)
                flag = 1
                break
        break

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "米飯"):
                food_intersection = list(set(food_list) & set(rice))
                protein_intersection = list(
                    set(protein_list) & set(rice_protein))
                carbs_intersection = list(set(carbs_list) & set(rice_carbs))
                fat_intersection = list(set(fat_list) & set(rice_fat))
                selected_food.remove("米飯")
                # print(selected_food)
                flag = 1
                break
        break

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "蔬菜"):
                food_intersection = list(set(food_list) & set(vegetable))
                protein_intersection = list(
                    set(protein_list) & set(vegetable_protein))
                carbs_intersection = list(
                    set(carbs_list) & set(vegetable_carbs))
                fat_intersection = list(set(fat_list) & set(vegetable_fat))
                selected_food.remove("蔬菜")
                # print(selected_food)
                flag = 1
                break
        break

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "豆腐"):
                food_intersection = list(set(food_list) & set(tofu))
                protein_intersection = list(
                    set(protein_list) & set(tofu_protein))
                carbs_intersection = list(set(carbs_list) & set(tofu_carbs))
                fat_intersection = list(set(fat_list) & set(tofu_fat))
                selected_food.remove("豆腐")
                # print(selected_food)
                flag = 1
                break
        break

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "豬肉"):
                food_intersection = list(set(food_list) & set(pork))
                protein_intersection = list(
                    set(protein_list) & set(pork_protein))
                carbs_intersection = list(set(carbs_list) & set(pork_carbs))
                fat_intersection = list(set(fat_list) & set(pork_fat))
                selected_food.remove("豬肉")
                # print(selected_food)
                flag = 1
                break
        break

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "雞肉"):
                food_intersection = list(set(food_list) & set(chicken))
                protein_intersection = list(
                    set(protein_list) & set(chicken_protein))
                carbs_intersection = list(set(carbs_list) & set(chicken_carbs))
                fat_intersection = list(set(fat_list) & set(chicken_fat))
                selected_food.remove("雞肉")
                # print(selected_food)
                flag = 1
                break
        break

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "牛肉"):
                food_intersection = list(set(food_list) & set(beef))
                protein_intersection = list(
                    set(protein_list) & set(beef_protein))
                carbs_intersection = list(set(carbs_list) & set(beef_carbs))
                fat_intersection = list(set(fat_list) & set(beef_fat))
                selected_food.remove("牛肉")
                # print(selected_food)
                flag = 1
                break
        break

    while (flag == 0):
        for i in range(len(selected_food)):
            if (selected_food[i] == "雞蛋"):
                food_intersection = list(set(food_list) & set(egg))
                protein_intersection = list(
                    set(protein_list) & set(egg_protein))
                carbs_intersection = list(set(carbs_list) & set(egg_carbs))
                fat_intersection = list(set(fat_list) & set(egg_fat))
                selected_food.remove("雞蛋")
                # print(selected_food)
                flag = 1
                break
        break

    calories_intersection = []
    # print(len(food_intersection))
    # print(len(protein_intersection))
    # print(len(carbs_intersection))
    # print(len(fat_intersection))
    for i in range(len(food_intersection)):
        calories_intersection.append(
            4*(protein_intersection[i]+carbs_intersection[i])+9*fat_intersection[i])

    return food_intersection, protein_intersection, carbs_intersection, fat_intersection, calories_intersection


def cal_error(n, food_list, protein_list, carbs_list, fat_list, calories_list, daily_calories, daily_protein, daily_carbs, daily_fat):

    # 限制條件
    calorie_limit = daily_calories/(n+1)
    # print(calorie_limit)
    protein_limit = daily_protein/(n+1)
    # print(protein_limit)
    carb_limit = daily_carbs/(n+1)
    # print(carb_limit)
    fat_limit = daily_fat/(n+1)
    # print(fat_limit)

    calories_error = []
    for i in range(len(calories_list)):
        calories_error.append((calories_list[i]-calorie_limit)**2)
    # print(calories_error)

    protein_error = []
    for i in range(len(protein_list)):
        protein_error.append((protein_list[i]-protein_limit)**2)
    # print(protein_error)

    carbs_error = []
    for i in range(len(carbs_list)):
        carbs_error.append((carbs_list[i]-carb_limit)**2)
    # print(carbs_error)

    fat_error = []
    for i in range(len(fat_list)):
        fat_error.append((fat_list[i]-fat_limit)**2)
    # print(fat_error)

    total_error = []
    for i in range(len(food_list)):
        total_error.append(
            calories_error[i]*1.5+protein_error[i]*1.2+carbs_error[i]+fat_error[i]*0.8)

    return (total_error)


def search_position(origin, food_suggest):
    # 地理編碼，獲取你的位置的經緯度座標
    geocode_result = gmaps.geocode(origin)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']

    place_name = []
    place_address = []
    place_rating = []
    distance_text = []

    for i in range(len(food_suggest)):
        # 地點搜尋，尋找最近且與關鍵字相關的地點
        places_result = gmaps.places_nearby(
            location=(lat, lng),
            keyword=food_suggest[i],
            radius=1000  # 搜尋半徑，以公尺為單位，可自行調整
        )

        # 找出最近的地點
        nearest_place = places_result['results'][0]
        place_name.append(nearest_place['name'])
        place_address.append(nearest_place['vicinity'])
        place_rating.append(nearest_place.get('rating', 'N/A'))

        # 使用 distance_matrix 函數計算兩個地點之間的距離
        distance_result = gmaps.distance_matrix(
            origins=(lat, lng),
            destinations=(nearest_place['geometry']['location']['lat'],
                          nearest_place['geometry']['location']['lng']),
            mode='driving'  # 設定出行模式，這裡使用駕車模式，可根據需要更改
        )

        # 提取距離資訊
        distance_text.append(
            distance_result['rows'][0]['elements'][0]['distance']['text'])
        distance_value = distance_result['rows'][0]['elements'][0]['distance']['value']

    return (place_name, place_address, place_rating, distance_text)


def main(page: ft.Page):
    page.title = "index"
    page.window_width = 600
    page.window_height = 600
    # page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # 置中

    def route_change(route):
        # page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(leading=ft.Icon(ft.icons.FASTFOOD), title=ft.Text(
                        "Don't know what to eat", size=25), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                    ft.Container(ft.Text("不知道要吃什麼？不用擔心！讓我們為您提供一些靈感", size=16,
                                 text_align=ft.TextAlign.CENTER), alignment=ft.alignment.center, margin=8),
                    ft.Container(ft.Text("無論您是想要中式美食還是西餐，還是尋找健康的選擇", size=16,
                                 text_align=ft.TextAlign.CENTER), alignment=ft.alignment.center, margin=8),
                    ft.Container(ft.Text("無論您的口味偏好如何，我們都能滿足您的需求！", size=16,
                                 text_align=ft.TextAlign.CENTER), alignment=ft.alignment.center, margin=8),
                    ft.Container(ft.Image(
                        src=f"./美食.jpg",
                        width=250,
                        height=250,
                        border_radius=ft.border_radius.all(60),
                        fit=ft.ImageFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT), alignment=ft.alignment.center, margin=10),
                    ft.Container(ft.ElevatedButton(content=ft.Text("開始", size=16), on_click=lambda _: page.go(
                        "/輸入基本資訊"), width=100, height=50), alignment=ft.alignment.bottom_right),
                ],
            )
        )

        def submit_daily(e):
            global daily_calories1, daily_protein1, daily_carbs1, daily_fat1
            daily_calories1, daily_protein1, daily_carbs1, daily_fat1 = calculate_daily_calories(
                gender.value, int(height.value), int(weight.value), int(age.value), activity_level.value)
            t1.value = (
                f"性別:{(gender.value)} 身高:{(height.value)} 體重:{(int(weight.value))} 年齡:{(int(age.value))} 活動水平:{(activity_level.value)}")
            page.update()

        if page.route == "/輸入基本資訊":

            gender = ft.RadioGroup(content=ft.Row([ft.Text("您的性別:", size=20), ft.Radio(
                value="male", label="男性"), ft.Radio(value="female", label="女性")], alignment=ft.MainAxisAlignment.CENTER))
            height = ft.TextField(label="您的身高", icon=ft.icons.EMOJI_PEOPLE,
                                  border_radius=10, suffix_text="cm", height=54)
            weight = ft.TextField(label="您的體重", icon=ft.icons.MONITOR_WEIGHT,
                                  border_radius=10, suffix_text="kg", height=54)
            age = ft.TextField(label="您的年齡", icon=ft.icons.ACCESS_TIME,
                               border_radius=10, suffix_text="yr", height=54)
            activity_level = ft.RadioGroup(content=ft.Column([ft.Row([ft.Radio(value="sedentary", label="缺乏運動"), ft.Radio(value="light", label="稍微運動"), ft.Radio(value="moderate", label="偶爾運動")], alignment=ft.MainAxisAlignment.CENTER),
                                                              ft.Row([ft.Radio(value="high", label="時常運動"), ft.Radio(value="very high", label="每天運動")], alignment=ft.MainAxisAlignment.CENTER)]))
            t1 = ft.Text("", size=16)

            page.views.append(
                ft.View(
                    "/輸入基本資訊",
                    [
                        ft.AppBar(leading=ft.Icon(ft.icons.MEDICAL_INFORMATION_ROUNDED), title=ft.Text(
                            "輸入基本資訊", size=25), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                        ft.Container(gender),
                        ft.Container(height),
                        ft.Container(weight),
                        ft.Container(age),
                        ft.Container(ft.Text("您的運動習慣", size=20),
                                     alignment=ft.alignment.center),
                        ft.Container(activity_level),
                        ft.Container(t1, alignment=ft.alignment.center),
                        ft.Row([
                            ft.Container(ft.ElevatedButton("上一頁", on_click=lambda _: page.go(
                                "/"), width=100, height=50), alignment=ft.alignment.bottom_left),
                            ft.Container(ft.ElevatedButton("送出", on_click=submit_daily, width=100, height=50,
                                         color='#220C4D', bgcolor='#D9E9D1'), alignment=ft.alignment.bottom_center),
                            ft.Container(ft.ElevatedButton("下一頁", on_click=lambda _: page.go(
                                "/您的基本資訊"), width=100, height=50), alignment=ft.alignment.bottom_right)
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=50),
                    ],
                )
            )

        if page.route == "/您的基本資訊":

            page.views.append(
                ft.View(
                    "/您的基本資訊",
                    [
                        ft.AppBar(leading=ft.Icon(ft.icons.PERM_DEVICE_INFORMATION), title=ft.Text(
                            "您的基本資訊", size=25), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                        ft.Container(ft.Text(
                            f"每天所需的總卡路里攝入量(calories):    {round(daily_calories1,2)}(kcal)", size=16), alignment=ft.alignment.center, margin=5),
                        ft.Container(ft.Text("每天所需的蛋白質攝入量(protein):        {:.2f}(g)".format(
                            daily_protein1), size=16), alignment=ft.alignment.center, margin=5),
                        ft.Container(ft.Text("每天所需的碳水化合物攝入量(carbs):      {:.2f}(g)".format(
                            daily_carbs1), size=16), alignment=ft.alignment.center, margin=5),
                        ft.Container(ft.Text("每天所需的脂肪攝入量(fat):              {:.2f}(g)".format(
                            daily_fat1), size=16), alignment=ft.alignment.center, margin=5),
                        ft.Container(ft.Image(
                            src=f"./2018每日飲食指南_飲食指南.png",
                            width=320,
                            height=240,
                            border_radius=ft.border_radius.all(60),
                            fit=ft.ImageFit.CONTAIN,
                            repeat=ft.ImageRepeat.NO_REPEAT), alignment=ft.alignment.center),
                        ft.Row([
                            ft.Container(ft.ElevatedButton("上一頁", on_click=lambda _: page.go(
                                "/輸入基本資訊"), width=100, height=50), alignment=ft.alignment.bottom_left),
                            ft.Container(ft.ElevatedButton("下一頁", on_click=lambda _: page.go(
                                "/輸入飲食偏好"), width=100, height=50), alignment=ft.alignment.bottom_right)
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=200),
                    ],
                )
            )

        def on_change_checkbox(e):
            if (meat_vegan.value == "1" or "3"):
                c5.disabled = False
                c6.disabled = False
                c7.disabled = False
                c8.disabled = False
            if (meat_vegan.value == "2"):
                c5.value = False
                c6.value = False
                c7.value = False
                c8.value = False
                c5.disabled = True
                c6.disabled = True
                c7.disabled = True
                c8.disabled = True
            page.update()

        def show_checkbox(e):
            global food_select
            food_select = []
            if (c1.value == True):
                food_select.append(c1.label)
            if (c2.value == True):
                food_select.append(c2.label)
            if (c3.value == True):
                food_select.append(c3.label)
            if (c4.value == True):
                food_select.append(c4.label)
            if (c5.value == True):
                food_select.append(c5.label)
            if (c6.value == True):
                food_select.append(c6.label)
            if (c7.value == True):
                food_select.append(c7.label)
            if (c8.value == True):
                food_select.append(c8.label)

            t3.value = food_select
            page.update()

        def cal_food_list(e):
            global food_list, ingredient_list, protein_list, carbs_list, fat_list, calories_list
            food_list = []
            ingredient_list = []
            protein_list = []
            carbs_list = []
            fat_list = []
            calories_list = []
            meat_vegan_decide(int(meat_vegan.value), food_list, ingredient_list,
                              protein_list, carbs_list, fat_list, calories_list)

            global food_list_new, protein_list_new, carbs_list_new, fat_list_new, calories_list_new, food_suggest
            food_list_new = []
            protein_list_new = []
            carbs_list_new = []
            fat_list_new = []
            calories_list_new = []
            food_suggest = []
            for i in range(len(food_select)):
                food_list_new, protein_list_new, carbs_list_new, fat_list_new, calories_list_new = food_classification_decide(
                    food_select, food_list, protein_list, carbs_list, fat_list)
                # 計算總誤差
                total_error = []
                total_error = cal_error(int(
                    n.value), food_list_new, protein_list_new, carbs_list_new, fat_list_new, calories_list_new, daily_calories1, daily_protein1, daily_carbs1, daily_fat1)
                # print(total_error)

                min_error = min(total_error)
                min_index = total_error.index(min_error)
                # print(food_list_new)
                # print(food_list_new[min_index])
                food_suggest.append(food_list_new[min_index])
            t4.value = food_suggest
            page.update()

        if page.route == "/輸入飲食偏好":
            meat_vegan = ft.RadioGroup(content=ft.Row([ft.Text("您的飲食習慣:", size=20), ft.Radio(value="1", label="葷"), ft.Radio(
                value="2", label="素"), ft.Radio(value="3", label="無特別限制")], alignment=ft.MainAxisAlignment.CENTER), on_change=on_change_checkbox)
            c1 = ft.Checkbox(label="麵條", value="麵條", on_change=show_checkbox)
            c2 = ft.Checkbox(label="米飯", value="米飯", on_change=show_checkbox)
            c3 = ft.Checkbox(label="蔬菜", value="蔬菜", on_change=show_checkbox)
            c4 = ft.Checkbox(label="豆腐", value="豆腐", on_change=show_checkbox)
            c5 = ft.Checkbox(label="豬肉", value="豬肉", on_change=show_checkbox)
            c6 = ft.Checkbox(label="雞肉", value="雞肉", on_change=show_checkbox)
            c7 = ft.Checkbox(label="牛肉", value="牛肉", on_change=show_checkbox)
            c8 = ft.Checkbox(label="雞蛋", value="雞蛋", on_change=show_checkbox)
            n = ft.Dropdown(width=100, height=60, options=[ft.dropdown.Option(1), ft.dropdown.Option(
                2), ft.dropdown.Option(3), ft.dropdown.Option(4), ft.dropdown.Option(5), ft.dropdown.Option(6)])
            t3 = ft.Text("", size=20)
            t4 = ft.Text("", size=20)
            page.views.append(
                ft.View(
                    "/輸入飲食偏好",
                    [
                        ft.AppBar(leading=ft.Icon(ft.icons.LOCAL_DRINK_OUTLINED), title=ft.Text(
                            "輸入飲食偏好", size=25), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                        ft.Container(
                            meat_vegan, alignment=ft.alignment.center),
                        ft.Row([ft.Container(
                            ft.Image(src=f"./FCF_2012322143.jpg",
                                width=100,
                                height=100,
                                border_radius=ft.border_radius.all(60),
                                fit=ft.ImageFit.CONTAIN,
                                repeat=ft.ImageRepeat.NO_REPEAT), alignment=ft.alignment.center_left),
                                ft.Column([ft.Text("您一天吃幾餐:"), n]),
                                ft.Container(ft.Image(src=f"./FCF_2012322143.jpg",
                                                      width=100,
                                                      height=100,
                                                      border_radius=ft.border_radius.all(
                                                          60),
                                                      fit=ft.ImageFit.CONTAIN,
                                                      repeat=ft.ImageRepeat.NO_REPEAT), alignment=ft.alignment.center_left)
                                ], alignment=ft.MainAxisAlignment.CENTER, spacing=55),
                        ft.Container(ft.Text("您喜歡的食物類別:(選三樣)", size=20),
                                     alignment=ft.alignment.center),
                        ft.Container(ft.Row(
                            [c1, c2, c3, c4], alignment=ft.MainAxisAlignment.CENTER), alignment=ft.alignment.center),
                        ft.Container(ft.Row(
                            [c5, c6, c7, c8], alignment=ft.MainAxisAlignment.CENTER), alignment=ft.alignment.center),
                        ft.Container(t3, alignment=ft.alignment.center),
                        ft.Container(t4, alignment=ft.alignment.center),
                        # ft.Text("  "),
                        # ft.Text("  "),
                        ft.Text("  "),
                        ft.Row([
                            ft.Container(ft.ElevatedButton("上一頁", on_click=lambda _: page.go(
                                "/您的基本資訊"), width=100, height=50), alignment=ft.alignment.bottom_left),
                            ft.Container(ft.ElevatedButton("送出", on_click=cal_food_list, width=100, height=50,
                                         color='#220C4D', bgcolor='#D9E9D1'), alignment=ft.alignment.bottom_center),
                            ft.Container(ft.ElevatedButton("下一頁", on_click=lambda _: page.go(
                                "/您的飲食偏好與結果"), width=100, height=50), alignment=ft.alignment.bottom_right)
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=50),
                    ],
                )
            )

        if page.route == "/您的飲食偏好與結果":

            position = ft.TextField(
                label="您的位置:", icon=ft.icons.NATURE_PEOPLE, border_radius=10)
            t1 = ft.Text("", size=14)
            t2 = ft.Text("", size=14)
            t3 = ft.Text("", size=14)
            t4 = ft.Text("", size=14)
            t5 = ft.Text("", size=14)
            t6 = ft.Text("", size=14)
            t7 = ft.Text("", size=14)
            t8 = ft.Text("", size=14)
            t9 = ft.Text("", size=14)
            t10 = ft.Text("", size=14)
            t11 = ft.Text("", size=14)
            t12 = ft.Text("", size=14)
            t13 = ft.Text("", size=14)
            t14 = ft.Text("", size=14)
            t15 = ft.Text("", size=14)
            t16 = ft.Text("", size=14)
            t17 = ft.Text("", size=14)
            t18 = ft.Text("", size=14)
            t19 = ft.Text("", size=14)
            t20 = ft.Text("", size=14)
            t21 = ft.Text("", size=14)
            t22 = ft.Text("", size=14)
            t23 = ft.Text("", size=14)
            t24 = ft.Text("", size=14)
            t25 = ft.Text("", size=14)
            t26 = ft.Text("", size=14)
            t27 = ft.Text("", size=14)
            t28 = ft.Text("", size=14)
            t29 = ft.Text("", size=14)
            t30 = ft.Text("", size=14)
            t31 = ft.Text("", size=14)
            t32 = ft.Text("", size=14)
            col1 = ft.Column([ft.Text("名稱", size=20), t1, t5, t9, t13,
                             t17, t21, t25, t29], alignment=ft.CrossAxisAlignment.CENTER)
            col2 = ft.Column([ft.Text("地點", size=20), t2, t6, t10, t14,
                             t18, t22, t26, t30], alignment=ft.CrossAxisAlignment.CENTER)
            col3 = ft.Column([ft.Text("評分", size=20), t3, t7, t11, t15,
                             t19, t23, t27, t31], alignment=ft.CrossAxisAlignment.CENTER)
            col4 = ft.Column([ft.Text("距離", size=20), t4, t8, t12, t16,
                             t20, t24, t28, t32], alignment=ft.CrossAxisAlignment.CENTER)

            def show_table(e):
                global place_name, place_address, place_rating, distance_text
                place_name = []
                place_address = []
                place_rating = []
                distance_text = []
                place_name, place_address, place_rating, distance_text = search_position(
                    position.value, food_suggest)

                t1.value = food_suggest[0]
                t2.value = place_name[0]
                t3.value = place_rating[0]
                t4.value = distance_text[0]
                if (food_suggest[1]):
                    t5.value = food_suggest[1]
                    t6.value = place_name[1]
                    t7.value = place_rating[1]
                    t8.value = distance_text[1]
                if (food_suggest[2]):
                    t9.value = food_suggest[2]
                    t10.value = place_name[2]
                    t11.value = place_rating[2]
                    t12.value = distance_text[2]
                # if (food_suggest[3]):
                #     t13.value = food_suggest[3]
                #     t14.value = place_name[3]
                #     t15.value = place_rating[3]
                #     t16.value = distance_text[3]
                # if (food_suggest[4]):
                #     t17.value = food_suggest[4]
                #     t18.value = place_name[4]
                #     t19.value = place_rating[4]
                #     t20.value = distance_text[4]
                # if (food_suggest[5]):
                #     t21.value = food_suggest[5]
                #     t22.value = place_name[5]
                #     t23.value = place_rating[5]
                #     t24.value = distance_text[5]
                # if (food_suggest[6]):
                #     t25.value = food_suggest[6]
                #     t26.value = place_name[6]
                #     t27.value = place_rating[6]
                #     t28.value = distance_text[6]
                # if (food_suggest[7]):
                #     t29.value = food_suggest[7]
                #     t30.value = place_name[7]
                #     t31.value = place_rating[7]
                #     t32.value = distance_text[7]

                page.update()

            page.views.append(
                ft.View(
                    "/您的飲食偏好與結果",
                    [
                        ft.AppBar(leading=ft.Icon(ft.icons.QUESTION_ANSWER_OUTLINED), title=ft.Text(
                            "您的飲食偏好與結果", size=25), bgcolor=ft.colors.SURFACE_VARIANT, center_title=True),
                        ft.Container(position, alignment=ft.alignment.center),
                        ft.Row([col1, col2, col3, col4], spacing=30,
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Text("  "),
                        ft.Text("  "),
                        ft.Row([
                            ft.Container(ft.ElevatedButton("上一頁", on_click=lambda _: page.go(
                                "/輸入飲食偏好"), width=100, height=50), alignment=ft.alignment.bottom_left),
                            ft.Container(ft.ElevatedButton("結果", on_click=show_table, width=100, height=50,
                                         color='#220C4D', bgcolor='#D9E9D1'), alignment=ft.alignment.bottom_center),
                            ft.Container(ft.ElevatedButton("再來一次", on_click=lambda _: page.go(
                                "/"), width=100, height=50), alignment=ft.alignment.bottom_right)
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=50),
                    ],
                )
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
