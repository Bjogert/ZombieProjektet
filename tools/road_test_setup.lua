-- Dedicated road-test map only. No gameplay or save changes outside this map.
local function prepareRoadTest(player)
    if not player or getWorld():getMap() ~= TEST_MAP then return end
    if player:getModData().RoadTestCarReady then return end
    local square = getCell():getGridSquare(START_X, START_Y, 0)
    if not square then return end
    local car = addVehicleDebug("Base.SUV", IsoDirections.N, nil, square)
    if not car then return end
    car:repair()
    local tank = car:getPartById("GasTank")
    if tank then tank:setContainerContentAmount(tank:getContainerCapacity()) end
    player:getInventory():AddItem(car:createVehicleKey())
    player:getModData().RoadTestCarReady = true
    print("ROAD_TEST car ready at " .. START_X .. "," .. START_Y)
end

Events.OnPlayerUpdate.Add(prepareRoadTest)
