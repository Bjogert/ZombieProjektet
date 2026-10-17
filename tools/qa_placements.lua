-- Read-only runtime checks for the synthetic placement fixture; excluded from packages.
local houses = {
    {id="west", x=120, y=120, turn=0}, {id="north", x=138, y=120, turn=1},
    {id="east", x=120, y=140, turn=2}, {id="south", x=138, y=140, turn=3},
}
local done, ticks = {}, 0
local function point(house, x, y)
    local w, h = 6, 10
    for i=1,house.turn do x,y,w,h = h-y-1,x,h,w end
    return house.x+x,house.y+y
end
local function report(house, label, actual, expected)
    print("[Placement QA] " .. (actual == expected and "PASS" or "FAIL") .. " " .. house.id
        .. " " .. label .. " actual=" .. tostring(actual) .. " expected=" .. tostring(expected))
end
local function check(house, player, cell)
    local width,height = 6,10
    if house.turn % 2 == 1 then width,height = 10,6 end
    -- Defer until the complete region is streamed. Never mutate world/player state.
    for y=house.y-6,house.y+height+6 do
        for x=house.x-6,house.x+width+6 do
            if not cell:getGridSquare(x,y,0) then return false end
        end
    end
    local indoors,ceiling,doors,windows,switches = 0,0,0,0,0
    local sprites = {}
    for y=house.y,house.y+height do
        for x=house.x,house.x+width do
            local sq = cell:getGridSquare(x,y,0)
            if x < house.x+width and y < house.y+height then
                if not sq:isOutside() then indoors=indoors+1 end
                local upper=cell:getGridSquare(x,y,1)
                if upper and upper:getFloor() then ceiling=ceiling+1 end
            end
            local objects=sq:getObjects()
            for i=0,objects:size()-1 do
                local obj=objects:get(i)
                if instanceof(obj,"IsoDoor") then doors=doors+1 end
                if instanceof(obj,"IsoWindow") then windows=windows+1 end
                if instanceof(obj,"IsoLightSwitch") then switches=switches+1 end
                local sprite=obj:getSprite()
                if sprite then
                    local name=sprite:getName()
                    if name then sprites[name]=(sprites[name] or 0)+1 end
                end
            end
        end
    end
    report(house,"indoor squares",indoors,60)
    report(house,"ceiling coverage",ceiling,60)
    report(house,"doors",doors,3)
    report(house,"windows",windows,7)
    report(house,"light switches",switches,3)
    local furniture={
        {"furniture_tables_low_01",{2,3,2,3},1},
        {"furniture_seating_indoor_01",{56,57,58,59},1},
        {"appliances_refrigeration_01",{0,3,2,1},1},
        {"appliances_cooking_01",{1,2,3,0},1},
        {"fixtures_sinks_01",{2,3,0,1},2},
        {"fixtures_bathroom_01",{0,2,3,1},1},
        {"furniture_bedding_01",{1,70,69,2},1},
        {"furniture_bedding_01",{0,71,68,3},1},
    }
    for _,item in ipairs(furniture) do
        local name=item[1].."_"..item[2][house.turn+1]
        report(house,name,sprites[name] or 0,item[3])
    end
    for _,edge in ipairs({{"west wall",0,5,-1,0},{"north wall",1,0,0,-1},
                         {"east wall",5,4,1,0},{"south wall",1,9,0,1}}) do
        local x,y=point(house,edge[2],edge[3])
        local tx,ty=point(house,edge[2]+edge[4],edge[3]+edge[5])
        report(house,edge[1],cell:getGridSquare(x,y,0):testCollideAdjacent(player,tx-x,ty-y,0),true)
    end
    local deck,outside,flowers,chairs,tables=0,0,0,0,0
    for ly=-2,11 do
        for lx=-5,6 do
            local x,y=point(house,lx,ly)
            local sq=cell:getGridSquare(x,y,0)
            if lx>=-4 and lx<=-1 and ly>=1 and ly<=6 then
                local floor=sq:getFloor()
                if floor and floor:getSprite():getName()=="carpentry_02_56" then deck=deck+1 end
                if sq:isOutside() then outside=outside+1 end
            end
            local objects=sq:getObjects()
            for i=0,objects:size()-1 do
                local sprite=objects:get(i):getSprite()
                local name=sprite and sprite:getName() or ""
                if name=="vegetation_ornamental_01_16" or name=="vegetation_ornamental_01_17"
                    or name=="vegetation_ornamental_01_18" then flowers=flowers+1 end
                if name=="furniture_seating_outdoor_01_"..({16,17,19,18})[house.turn+1]
                    or name=="furniture_seating_outdoor_01_"..({19,18,16,17})[house.turn+1] then chairs=chairs+1 end
                if name=="furniture_tables_low_01_"..({21,20,21,20})[house.turn+1] then tables=tables+1 end
            end
        end
    end
    report(house,"deck floors",deck,24)
    report(house,"deck outdoors",outside,24)
    report(house,"flower tiles",flowers,11)
    report(house,"outdoor chairs",chairs,2)
    report(house,"outdoor table",tables,1)
    local edges,blocked={},0
    for x=-1,5 do
        table.insert(edges,{x,-1,x+1,-1})
        table.insert(edges,{x,10,x+1,10})
    end
    for y=-1,9 do
        table.insert(edges,{-1,y,-1,y+1})
        table.insert(edges,{6,y,6,y+1})
    end
    for x=-5,-2 do table.insert(edges,{x,3,x+1,3}) end
    for _,edge in ipairs(edges) do
        local x,y=point(house,edge[1],edge[2])
        local tx,ty=point(house,edge[3],edge[4])
        if cell:getGridSquare(x,y,0):testCollideAdjacent(player,tx-x,ty-y,0) then blocked=blocked+1 end
    end
    report(house,"blocked garden access edges",blocked,0)
    return true
end
local function run()
    ticks=ticks+1
    if ticks % 60 ~= 0 then return end
    local player,cell=getSpecificPlayer(0),getCell()
    if not player or not cell then return end
    for _,house in ipairs(houses) do
        if not done[house.id] and check(house,player,cell) then done[house.id]=true end
    end
end
Events.OnTick.Add(run)
