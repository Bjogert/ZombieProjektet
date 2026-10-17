-- Read-only COTTAGE-02 runtime evidence. Never included in the package.
local function report(label, actual, expected)
    print("[Garden QA] " .. (actual == expected and "PASS" or "FAIL") .. " " .. label
        .. " actual=" .. tostring(actual) .. " expected=" .. tostring(expected))
end

local function runChecks()
    local player, cell = getSpecificPlayer(0), getCell()
    if not player or not cell or player:getX() < 110 or player:getX() > 140
        or player:getY() < 110 or player:getY() > 140 then return end
    local floors, outdoors, flowers, chairs, tables = 0, 0, 0, 0, 0
    for y = 118, 131 do
        for x = 115, 126 do
            local square = cell:getGridSquare(x, y, 0)
            if square then
                if x >= 116 and x <= 119 and y >= 121 and y <= 126 then
                    local floor = square:getFloor()
                    if floor and floor:getSprite():getName() == "carpentry_02_56" then
                        floors = floors + 1
                    end
                    if square:isOutside() then outdoors = outdoors + 1 end
                end
                local objects = square:getObjects()
                for i = 0, objects:size() - 1 do
                    local sprite = objects:get(i):getSprite()
                    local name = sprite and sprite:getName() or ""
                    if name == "vegetation_ornamental_01_16" or name == "vegetation_ornamental_01_17"
                        or name == "vegetation_ornamental_01_18" then flowers = flowers + 1 end
                    if name == "furniture_seating_outdoor_01_16" or name == "furniture_seating_outdoor_01_19" then
                        chairs = chairs + 1
                    end
                    if name == "furniture_tables_low_01_21" then tables = tables + 1 end
                end
            end
        end
    end
    report("wooden deck floors", floors, 24)
    report("deck remains outdoors", outdoors, 24)
    report("flowerbed tiles", flowers, 11)
    report("outdoor chairs", chairs, 2)
    report("outdoor table", tables, 1)
    local blocked = 0
    -- Contiguous ring around the house plus the path across the deck.
    local edges = {}
    for x = 119, 125 do
        table.insert(edges, {x, 119, 1, 0})
        table.insert(edges, {x, 130, 1, 0})
    end
    for y = 119, 129 do
        table.insert(edges, {119, y, 0, 1})
        table.insert(edges, {126, y, 0, 1})
    end
    for x = 114, 118 do table.insert(edges, {x, 123, 1, 0}) end
    for _, edge in ipairs(edges) do
        local square = cell:getGridSquare(edge[1], edge[2], 0)
        if not square or square:testCollideAdjacent(player, edge[3], edge[4], 0) then
            blocked = blocked + 1
        end
    end
    report("blocked edges on access routes", blocked, 0)
    local approach = cell:getGridSquare(117, 124, 0)
    report("table collision", approach and approach:testCollideAdjacent(player, 0, 1, 0), true)
end
Events.OnGameStart.Add(runChecks)
